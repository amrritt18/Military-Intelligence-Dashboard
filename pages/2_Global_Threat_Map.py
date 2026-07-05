import streamlit as st

from utils.loaders import load_dataset
from utils.visualization import create_world_map


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Global Threat Map",
    page_icon="🌍",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Page Title
# ==========================================

st.title("🌍 Global Threat Map")

st.markdown("""
Visualize global terrorist incidents using the **Global Terrorism Database (GTD)**.
Use the filter in the sidebar to explore incidents by year.
""")


# ==========================================
# Sidebar Filters
# ==========================================

st.sidebar.header("🔍 Filters")

year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["iyear"].unique().tolist())
)

if year != "All":
    df = df[df["iyear"] == year]


# ==========================================
# Remove Missing Coordinates
# ==========================================

df = df.dropna(subset=["latitude", "longitude"])


# ==========================================
# Global Threat Map
# ==========================================

fig = create_world_map(
    df=df,
    title="Global Terrorist Incidents",
    color="attacktype1_txt",
    hover_name="country_txt",
    hover_data={
        "city": True,
        "gname": True,
        "nkill": True,
        "latitude": False,
        "longitude": False
    }
)

st.plotly_chart(fig, use_container_width=True)


# ==========================================
# Summary
# ==========================================

st.metric(
    "Displayed Incidents",
    f"{len(df):,}"
)

st.info("👈 Use the sidebar filter to visualize incidents for a specific year.")