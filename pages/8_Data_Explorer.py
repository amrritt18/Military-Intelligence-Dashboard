import streamlit as st

from utils.loaders import load_dataset
from utils.helpers import (
    safe_sum,
    dataframe_to_csv
)
from utils.visualization import (
    create_bar_chart,
    create_pie_chart,
    create_horizontal_bar_chart
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Data Explorer",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Page Title
# ==========================================

st.title("📊 Global Terrorism Data Explorer")

st.markdown("""
Explore, filter, visualize and download the Global Terrorism Database (GTD).
""")


# ==========================================
# Sidebar Filters
# ==========================================

st.sidebar.header("Dataset Filters")

years = sorted(df["iyear"].dropna().unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years
)

countries = sorted(df["country_txt"].dropna().unique())

selected_country = st.sidebar.multiselect(
    "Select Country",
    countries
)

regions = sorted(df["region_txt"].dropna().unique())

selected_region = st.sidebar.multiselect(
    "Select Region",
    regions
)

attack_types = sorted(df["attacktype1_txt"].dropna().unique())

selected_attack = st.sidebar.multiselect(
    "Attack Type",
    attack_types
)

weapon_types = sorted(df["weaptype1_txt"].dropna().unique())

selected_weapon = st.sidebar.multiselect(
    "Weapon Type",
    weapon_types
)

groups = sorted(df["gname"].dropna().unique())

selected_group = st.sidebar.multiselect(
    "Terrorist Group",
    groups
)


# ==========================================
# Apply Filters
# ==========================================

filtered_df = df.copy()

if selected_year:

    filtered_df = filtered_df[
        filtered_df["iyear"].isin(selected_year)
    ]

if selected_country:

    filtered_df = filtered_df[
        filtered_df["country_txt"].isin(selected_country)
    ]

if selected_region:

    filtered_df = filtered_df[
        filtered_df["region_txt"].isin(selected_region)
    ]

if selected_attack:

    filtered_df = filtered_df[
        filtered_df["attacktype1_txt"].isin(selected_attack)
    ]

if selected_weapon:

    filtered_df = filtered_df[
        filtered_df["weaptype1_txt"].isin(selected_weapon)
    ]

if selected_group:

    filtered_df = filtered_df[
        filtered_df["gname"].isin(selected_group)
    ]


# ==========================================
# Search
# ==========================================

search = st.text_input(
    "🔍 Search by Country, City or Terrorist Group"
)

if search:

    filtered_df = filtered_df[

        filtered_df["country_txt"]
        .fillna("")
        .str.contains(search, case=False)

        |

        filtered_df["city"]
        .fillna("")
        .str.contains(search, case=False)

        |

        filtered_df["gname"]
        .fillna("")
        .str.contains(search, case=False)

    ]


# ==========================================
# Dataset Summary
# ==========================================

st.subheader("📊 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Incidents",
    len(filtered_df)
)

col2.metric(
    "Countries",
    filtered_df["country_txt"].nunique()
)

col3.metric(
    "Fatalities",
    safe_sum(filtered_df["nkill"])
)

col4.metric(
    "Injuries",
    safe_sum(filtered_df["nwound"])
)

st.divider()


# ==========================================
# Dataset Preview
# ==========================================

st.subheader("📋 Dataset Preview")

selected_columns = st.multiselect(
    "Select Columns",
    filtered_df.columns.tolist(),
    default=filtered_df.columns.tolist()[:10]
)

if selected_columns:

    st.dataframe(
        filtered_df[selected_columns],
        use_container_width=True,
        height=500
    )

st.divider()


# ==========================================
# Download Dataset
# ==========================================

csv = dataframe_to_csv(filtered_df)

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="Filtered_GTD_Data.csv",
    mime="text/csv"
)

st.divider()

# ==========================================
# Visual Analytics
# ==========================================

st.subheader("📈 Visual Analytics")

tab1, tab2, tab3 = st.tabs(
    [
        "Country",
        "Attack Type",
        "Weapon Type"
    ]
)


# ==========================================
# Country Analysis
# ==========================================

with tab1:

    country_chart = (

        filtered_df
        .groupby("country_txt")
        .size()
        .reset_index(name="Incidents")
        .sort_values(
            "Incidents",
            ascending=False
        )
        .head(10)

    )

    fig = create_bar_chart(

        country_chart,
        x="country_txt",
        y="Incidents",
        title="Top 10 Countries by Incidents"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================
# Attack Types
# ==========================================

with tab2:

    attack_chart = (

        filtered_df
        .groupby("attacktype1_txt")
        .size()
        .reset_index(name="Count")

    )

    fig = create_pie_chart(

        attack_chart,
        names="attacktype1_txt",
        values="Count",
        title="Attack Type Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================
# Weapon Types
# ==========================================

with tab3:

    weapon_chart = (

        filtered_df
        .groupby("weaptype1_txt")
        .size()
        .reset_index(name="Count")
        .sort_values(
            "Count",
            ascending=False
        )

    )

    fig = create_horizontal_bar_chart(

        weapon_chart,
        x="Count",
        y="weaptype1_txt",
        title="Weapon Type Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()


# ==========================================
# Missing Value Analysis
# ==========================================

st.subheader("📉 Missing Value Analysis")

missing = (

    filtered_df
    .isnull()
    .sum()
    .reset_index()

)

missing.columns = [

    "Column",
    "Missing Values"

]

missing = missing.sort_values(
    "Missing Values",
    ascending=False
)

st.dataframe(
    missing,
    use_container_width=True
)

top_missing = missing.head(15)

fig = create_horizontal_bar_chart(

    top_missing,
    x="Missing Values",
    y="Column",
    title="Top 15 Columns with Missing Values"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# ==========================================
# Statistical Summary
# ==========================================

st.subheader("📊 Statistical Summary")

st.dataframe(

    filtered_df.describe(
        include="all"
    ),

    use_container_width=True

)

st.divider()


# ==========================================
# Dataset Information
# ==========================================

st.subheader("ℹ️ Dataset Information")

info1, info2, info3, info4 = st.columns(4)

info1.metric(
    "Rows",
    filtered_df.shape[0]
)

info2.metric(
    "Columns",
    filtered_df.shape[1]
)

memory_usage = round(

    filtered_df.memory_usage(
        deep=True
    ).sum() / 1024**2,

    2

)

info3.metric(
    "Memory (MB)",
    memory_usage
)

numeric_columns = filtered_df.select_dtypes(
    include="number"
).shape[1]

info4.metric(
    "Numeric Columns",
    numeric_columns
)

st.divider()


# ==========================================
# Column Names
# ==========================================

st.subheader("📝 Dataset Columns")

st.write(
    filtered_df.columns.tolist()
)