import streamlit as st


# Page Configuration

st.set_page_config(
    page_title="AI Military Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide",
)


# Main Title


st.title("🛡️ AI-Based Military Intelligence Dashboard")


st.markdown(
    """
Welcome to the **AI-Based Military Intelligence Dashboard**.

This application provides interactive visualizations, predictive analytics,
and AI-powered intelligence using the **Global Terrorism Database (GTD)**.

Use the navigation menu on the left to explore different modules.
"""
)


# Dashboard Modules


st.subheader("📂 Available Modules")

st.markdown(
    """
- 🏠 Home
- 🌍 Global Threat Map
- 🌎 Country Analysis
- 🤖 Attack Prediction
- ⚠️ Threat Level Prediction
- 📈 Forecasting
- 📝 AI Intelligence Report
- 🔍 Data Explorer
- ⚙️ Settings
"""
)


st.success("👈 Select a page from the left sidebar to get started.")