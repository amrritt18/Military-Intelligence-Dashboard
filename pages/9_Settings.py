import streamlit as st
import platform
import sys

from utils.loaders import load_dataset


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Dashboard Information",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# Load Dataset
# ==========================================

df = load_dataset()


# ==========================================
# Page Title
# ==========================================

st.title("⚙️ Dashboard Information")

st.markdown("""
This page provides information about the AI-Based Military Intelligence Dashboard,
its dataset, machine learning models, forecasting model, and system environment.
""")


# ==========================================
# Dashboard Overview
# ==========================================

st.header("📋 Dashboard Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Dashboard Version",
    "1.0"
)

col2.metric(
    "Pages",
    "9"
)

col3.metric(
    "Utility Modules",
    "6"
)

st.divider()


# ==========================================
# Dataset Information
# ==========================================

st.header("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Rows",
    f"{df.shape[0]:,}"
)

col2.metric(
    "Columns",
    df.shape[1]
)

col3.metric(
    "Countries",
    df["country_txt"].nunique()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Regions",
    df["region_txt"].nunique()
)

col2.metric(
    "Attack Types",
    df["attacktype1_txt"].nunique()
)

col3.metric(
    "Weapon Types",
    df["weaptype1_txt"].nunique()
)

st.divider()


# ==========================================
# Machine Learning Models
# ==========================================

st.header("🤖 Machine Learning Models")

st.success("✅ Attack Type Prediction Model")

st.write("- Algorithm : Random Forest Classifier")

st.write("- Output : Attack Type Prediction")

st.success("✅ Threat Level Prediction Model")

st.write("- Algorithm : Random Forest Classifier")

st.write("- Output : LOW / MEDIUM / HIGH")

st.success("✅ Forecasting Model")

st.write("- Algorithm : Prophet Time Series Forecasting")

st.write("- Output : Future Attack Trend")

st.divider()


# ==========================================
# Dashboard Features
# ==========================================

st.header("🚀 Dashboard Features")

features = [

    "🏠 Home Dashboard",

    "🌍 Global Threat Map",

    "🌎 Country Analysis",

    "🤖 Attack Type Prediction",

    "🚨 Threat Level Prediction",

    "📈 Prophet Forecasting",

    "🧠 AI Intelligence Report",

    "📊 Data Explorer",

    "📥 CSV Export"

]

for feature in features:

    st.write(feature)

st.divider()


# ==========================================
# Technologies Used
# ==========================================

st.header("💻 Technologies")

tech1, tech2 = st.columns(2)

with tech1:

    st.markdown("""
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
""")

with tech2:

    st.markdown("""
- Prophet
- Plotly
- Joblib
- Git
- GitHub
""")

st.divider()


# ==========================================
# System Information
# ==========================================

st.header("🖥️ System Information")

info1, info2 = st.columns(2)

with info1:

    st.write(f"**Python Version:** {sys.version.split()[0]}")

    st.write(f"**Platform:** {platform.system()}")

    st.write(f"**Release:** {platform.release()}")

with info2:

    st.write(f"**Processor:** {platform.processor()}")

    st.write(f"**Machine:** {platform.machine()}")

st.divider()


# ==========================================
# Project Structure
# ==========================================

st.header("📁 Project Structure")

st.code(
"""
Military-Intelligence-Dashboard/

├── app.py
├── data/
├── models/
├── pages/
├── utils/
├── train_attack_model.py
├── train_threat_model.py
├── requirements.txt
└── README.md
""",
language="text"
)

st.divider()


# ==========================================
# About Project
# ==========================================

st.header("ℹ️ About")

st.info(
"""
This dashboard was developed as an AI and Machine Learning project
using the Global Terrorism Database (GTD).

It combines:

• Machine Learning

• Time Series Forecasting

• Interactive Data Visualization

• Threat Analysis

• AI-assisted Intelligence Reporting

to support terrorism data exploration and decision support.
"""
)

st.divider()


# ==========================================
# Status
# ==========================================

st.success("✅ Dataset Loaded Successfully")

st.success("✅ Machine Learning Models Ready")

st.success("✅ Forecasting Model Ready")

st.success("✅ Dashboard Running Successfully")