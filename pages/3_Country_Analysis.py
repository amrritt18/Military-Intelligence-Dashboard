import streamlit as st

from utils.loaders import load_dataset
from utils.visualization import (
    create_line_chart,
    create_bar_chart,
    create_horizontal_bar_chart,
    create_pie_chart,
    create_world_map
)
from utils.helpers import safe_sum, dataframe_to_csv


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Country Analysis",
    page_icon="🌎",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Sidebar
# ==========================================

st.title("🌎 Country Analysis")

countries = sorted(df["country_txt"].dropna().unique())

country = st.sidebar.selectbox(
    "Select Country",
    countries
)

country_df = df[df["country_txt"] == country]

st.header(f"📊 Intelligence Report : {country}")


# ==========================================
# Dashboard Summary
# ==========================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Incidents",
    f"{len(country_df):,}"
)

col2.metric(
    "Fatalities",
    f"{safe_sum(country_df['nkill']):,}"
)

col3.metric(
    "Injured",
    f"{safe_sum(country_df['nwound']):,}"
)

col4.metric(
    "Groups",
    country_df["gname"].nunique()
)

st.divider()


# ==========================================
# Attacks Over Time
# ==========================================

left, right = st.columns(2)

with left:

    yearly = (
        country_df
        .groupby("iyear")
        .size()
        .reset_index(name="Attacks")
    )

    fig = create_line_chart(
        yearly,
        x="iyear",
        y="Attacks",
        title="Attacks Over Years"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    attack = (
        country_df
        .groupby("attacktype1_txt")
        .size()
        .reset_index(name="Count")
    )

    fig = create_pie_chart(
        attack,
        names="attacktype1_txt",
        values="Count",
        title="Attack Types"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()


# ==========================================
# Organizations
# ==========================================

left, right = st.columns(2)

with left:

    groups = (
        country_df
        .groupby("gname")
        .size()
        .reset_index(name="Attacks")
        .sort_values("Attacks", ascending=False)
        .head(10)
    )

    fig = create_horizontal_bar_chart(
        groups,
        x="Attacks",
        y="gname",
        title="Top Terrorist Organizations"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    weapon = (
        country_df
        .groupby("weaptype1_txt")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
    )

    fig = create_bar_chart(
        weapon,
        x="weaptype1_txt",
        y="Count",
        title="Weapon Types"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================
# Incident Map
# ==========================================

st.subheader("🌍 Incident Locations")

map_df = country_df.dropna(
    subset=["latitude", "longitude"]
)

fig = create_world_map(
    df=map_df,
    title=f"Terrorist Incidents in {country}",
    color="attacktype1_txt",
    hover_name="city",
    hover_data={
        "country_txt": True,
        "iyear": True,
        "attacktype1_txt": True,
        "gname": True,
        "nkill": True,
        "latitude": False,
        "longitude": False
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# ==========================================
# Incident Details
# ==========================================

st.subheader("📋 Incident Details")

columns = [
    "iyear",
    "city",
    "attacktype1_txt",
    "targtype1_txt",
    "weaptype1_txt",
    "gname",
    "nkill",
    "nwound"
]

st.dataframe(
    country_df[columns],
    use_container_width=True
)

st.divider()


# ==========================================
# Download Data
# ==========================================

csv = dataframe_to_csv(country_df)

st.download_button(
    label="⬇ Download Country Data",
    data=csv,
    file_name=f"{country}.csv",
    mime="text/csv"
)