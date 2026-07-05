import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from prophet import Prophet

from utils.loaders import load_dataset
from utils.helpers import dataframe_to_csv


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Forecasting",
    page_icon="📈",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Page Title
# ==========================================

st.title("📈 Terrorism Attack Forecasting")

st.markdown("""
Forecast future terrorist incidents using historical GTD data and the **Prophet Time Series Forecasting Model**.
""")


# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("Forecast Settings")

countries = sorted(
    df["country_txt"].dropna().unique()
)

country = st.sidebar.selectbox(
    "Select Country",
    countries
)

forecast_years = st.sidebar.slider(
    "Forecast Years",
    1,
    10,
    5
)


# ==========================================
# Prepare Dataset
# ==========================================

country_df = df[
    df["country_txt"] == country
]

yearly = (
    country_df
    .groupby("iyear")
    .size()
    .reset_index(name="Attacks")
)

yearly = yearly.sort_values("iyear")


# ==========================================
# Check Data
# ==========================================

if len(yearly) < 5:

    st.warning(
        "Not enough historical data available for forecasting."
    )

    st.stop()


# ==========================================
# Prepare Prophet Dataset
# ==========================================

prophet_df = yearly.rename(
    columns={
        "iyear": "ds",
        "Attacks": "y"
    }
)

prophet_df["ds"] = pd.to_datetime(
    prophet_df["ds"],
    format="%Y"
)


# ==========================================
# Train Prophet Model
# ==========================================

model = Prophet()

model.fit(
    prophet_df
)


# ==========================================
# Create Future Data
# ==========================================

future = model.make_future_dataframe(
    periods=forecast_years,
    freq="YS"
)

forecast_prophet = model.predict(
    future
)

forecast = forecast_prophet.tail(
    forecast_years
).copy()

forecast["Year"] = (
    forecast["ds"]
    .dt.year
)

forecast["Forecasted Attacks"] = (
    forecast["yhat"]
    .clip(lower=0)
    .round()
    .astype(int)
)


# ==========================================
# Forecast Chart
# ==========================================

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=prophet_df["ds"].dt.year,
        y=prophet_df["y"],
        mode="markers",
        name="Historical Data"
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_prophet["ds"].dt.year,
        y=forecast_prophet["yhat"],
        mode="lines",
        name="Prophet Trend"
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast["Year"],
        y=forecast["Forecasted Attacks"],
        mode="lines+markers",
        name="Future Forecast"
    )
)

fig.update_layout(
    title=f"Forecast for {country}",
    xaxis_title="Year",
    yaxis_title="Number of Attacks",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# ==========================================
# Forecast Results
# ==========================================

st.subheader("Forecast Results")

st.dataframe(
    forecast[
        [
            "Year",
            "Forecasted Attacks",
            "yhat_lower",
            "yhat_upper"
        ]
    ],
    use_container_width=True
)

st.divider()

# ==========================================
# Growth Analysis
# ==========================================

historical_last = yearly.iloc[-1]["Attacks"]

forecast_last = forecast["Forecasted Attacks"].iloc[-1]

growth = (
    (forecast_last - historical_last)
    / max(historical_last, 1)
) * 100

st.subheader("📊 Growth Analysis")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Current Attacks",
    int(historical_last)
)

col2.metric(
    f"Forecast ({forecast_years} Years)",
    int(forecast_last)
)

col3.metric(
    "Growth %",
    f"{growth:.2f}%"
)

st.divider()


# ==========================================
# Risk Assessment
# ==========================================

st.subheader("🚨 Risk Assessment")

if growth < 0:

    st.success("🟢 Threat Trend : Decreasing")

elif growth < 15:

    st.warning("🟡 Threat Trend : Stable")

else:

    st.error("🔴 Threat Trend : Increasing")

st.divider()


# ==========================================
# Forecast Confidence Interval
# ==========================================

st.subheader("📉 Forecast Confidence Interval")

confidence_fig = go.Figure()

confidence_fig.add_trace(
    go.Scatter(
        x=forecast["Year"],
        y=forecast["yhat_upper"],
        mode="lines",
        line=dict(width=0),
        showlegend=False
    )
)

confidence_fig.add_trace(
    go.Scatter(
        x=forecast["Year"],
        y=forecast["yhat_lower"],
        mode="lines",
        fill="tonexty",
        name="Confidence Interval"
    )
)

confidence_fig.add_trace(
    go.Scatter(
        x=forecast["Year"],
        y=forecast["Forecasted Attacks"],
        mode="lines+markers",
        name="Forecast"
    )
)

confidence_fig.update_layout(
    title="Forecast Uncertainty",
    xaxis_title="Year",
    yaxis_title="Expected Number of Attacks",
    height=500
)

st.plotly_chart(
    confidence_fig,
    use_container_width=True
)

st.divider()


# ==========================================
# Download Forecast
# ==========================================

csv = dataframe_to_csv(

    forecast[
        [
            "Year",
            "Forecasted Attacks",
            "yhat_lower",
            "yhat_upper"
        ]
    ]

)

st.download_button(
    label="📥 Download Forecast CSV",
    data=csv,
    file_name=f"{country}_forecast.csv",
    mime="text/csv"
)