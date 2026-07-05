import streamlit as st

from utils.loaders import load_dataset
from utils.helpers import (
    safe_sum,
    dataframe_to_csv
)
from utils.visualization import (
    create_horizontal_bar_chart,
    create_pie_chart
)
from utils.report_generator import generate_report


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Intelligence Report",
    page_icon="🧠",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Page Title
# ==========================================

st.title("🧠 AI Intelligence Report")

st.markdown("""
Generate an AI-assisted intelligence summary using the
Global Terrorism Database (GTD).
""")


# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("Report Filters")

years = sorted(
    df["iyear"].unique()
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + list(years)
)

if selected_year != "All":

    df = df[
        df["iyear"] == selected_year
    ]


# ==========================================
# Dashboard Statistics
# ==========================================

total_incidents = len(df)

total_killed = safe_sum(
    df["nkill"]
)

total_wounded = safe_sum(
    df["nwound"]
)

countries = df["country_txt"].nunique()

groups = df["gname"].nunique()


# ==========================================
# Threat Assessment
# ==========================================

impact = (
    total_killed +
    total_wounded
) / max(
    total_incidents,
    1
)

if impact < 2:

    threat = "LOW 🟢"

elif impact < 5:

    threat = "MEDIUM 🟡"

else:

    threat = "HIGH 🔴"


# ==========================================
# Dashboard Metrics
# ==========================================

st.subheader("📊 Intelligence Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Incidents",
    f"{total_incidents:,}"
)

col2.metric(
    "Fatalities",
    f"{total_killed:,}"
)

col3.metric(
    "Injuries",
    f"{total_wounded:,}"
)

col4.metric(
    "Threat Level",
    threat
)

st.divider()


# ==========================================
# Top Countries
# ==========================================

top_countries = (

    df
    .groupby("country_txt")
    .size()
    .reset_index(name="Incidents")
    .sort_values(
        "Incidents",
        ascending=False
    )
    .head(10)

)

fig = create_horizontal_bar_chart(

    top_countries,
    x="Incidents",
    y="country_txt",
    title="Top 10 High-Risk Countries"

)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ==========================================
# Top Terrorist Groups
# ==========================================

top_groups = (

    df
    .groupby("gname")
    .size()
    .reset_index(name="Attacks")
    .sort_values(
        "Attacks",
        ascending=False
    )
    .head(10)

)

fig = create_horizontal_bar_chart(

    top_groups,
    x="Attacks",
    y="gname",
    title="Most Active Terrorist Organizations"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================
# Attack Type Distribution
# ==========================================

attack_types = (

    df
    .groupby("attacktype1_txt")
    .size()
    .reset_index(name="Count")
    .sort_values(
        "Count",
        ascending=False
    )

)

fig = create_pie_chart(

    attack_types,
    names="attacktype1_txt",
    values="Count",
    title="Attack Type Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# ==========================================
# Executive Summary
# ==========================================

st.subheader("📄 Executive Summary")

summary = f"""
### Intelligence Overview

- **Total Incidents:** {total_incidents:,}
- **Countries Affected:** {countries}
- **Fatalities:** {total_killed:,}
- **Injuries:** {total_wounded:,}
- **Threat Level:** {threat}

**Highest Risk Country:** {top_countries.iloc[0]['country_txt']}

**Most Active Terrorist Organization:** {top_groups.iloc[0]['gname']}

This assessment is generated from historical records available in the Global Terrorism Database (GTD).
"""

st.info(summary)

st.divider()


# ==========================================
# AI Intelligence Report
# ==========================================

st.subheader("🧠 AI Intelligence Assessment")

report = generate_report(

    top_countries.iloc[0]["country_txt"],
    total_incidents,
    total_killed,
    total_wounded,
    groups

)

st.success(report)

st.divider()


# ==========================================
# Strategic Recommendations
# ==========================================

st.subheader("🎯 Strategic Recommendations")

st.markdown(f"""
1. Increase surveillance and intelligence gathering in **{top_countries.iloc[0]['country_txt']}**.

2. Closely monitor activities related to **{top_groups.iloc[0]['gname']}**.

3. Strengthen protection of high-value civilian and government infrastructure.

4. Improve intelligence sharing between national and international security agencies.

5. Increase monitoring of regions with frequent attacks involving **{attack_types.iloc[0]['attacktype1_txt']}**.

6. Continue predictive analysis using AI and Machine Learning models to identify emerging threats.
""")

st.divider()


# ==========================================
# Download AI Report
# ==========================================

st.download_button(

    label="📄 Download Intelligence Report",

    data=report,

    file_name="AI_Intelligence_Report.txt",

    mime="text/plain"

)

st.divider()


# ==========================================
# Download Filtered Dataset
# ==========================================

csv = dataframe_to_csv(df)

st.download_button(

    label="📥 Download Filtered Dataset",

    data=csv,

    file_name="Filtered_GTD_Data.csv",

    mime="text/csv"

)