import streamlit as st

from utils.loaders import load_dataset
from utils.visualization import create_line_chart
from utils.helpers import safe_sum, format_number


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Dashboard Title
# ==========================================

st.title("🏠 Home")

st.markdown("""
Welcome to the **AI-Based Military Intelligence Dashboard**.

This dashboard provides military intelligence analysis, interactive visualizations,
and AI-powered insights using the Global Terrorism Database (GTD).
""")


# ==========================================
# Dashboard Summary
# ==========================================

st.subheader("📊 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Incidents", format_number(len(df)))
col2.metric("Total Fatalities", format_number(safe_sum(df["nkill"])))
col3.metric("Total Injured", format_number(safe_sum(df["nwound"])))
col4.metric("Countries", format_number(df["country_txt"].nunique()))

st.divider()


# ==========================================
# Attacks Over Years
# ==========================================

st.subheader("📈 Terrorist Attacks Over the Years")

yearly = (
    df.groupby("iyear")
    .size()
    .reset_index(name="Attacks")
)

fig = create_line_chart(
    yearly,
    x="iyear",
    y="Attacks",
    title="Global Terrorist Incidents by Year"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()


# ==========================================
# Quick Information
# ==========================================

st.info("""
### Dashboard Modules

- 🏠 Home
- 🌍 Global Threat Map
- 🌎 Country Analysis
- 🤖 Attack Prediction
- ⚠️ Threat Level Prediction
- 📈 Forecasting
- 📝 AI Intelligence Report
- 🔍 Data Explorer
- ⚙️ Settings

Use the left sidebar to explore each module.
""")