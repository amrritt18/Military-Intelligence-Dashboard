import streamlit as st
import pandas as pd

from utils.loaders import load_dataset, load_threat_prediction_model
from utils.preprocessing import clean_prediction_data, encode_threat_features
from utils.prediction import predict_attack, prediction_probability, decode_prediction
from utils.helpers import calculate_confidence


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Threat Level Prediction",
    page_icon="🚨",
    layout="wide"
)


# ==========================================
# Load Dataset & Model
# ==========================================

df = load_dataset()

model, encoders, target_encoder = load_threat_prediction_model()


# ==========================================
# Data Preprocessing
# ==========================================

required_columns = [
    "country_txt",
    "region_txt",
    "attacktype1_txt",
    "weaptype1_txt",
    "targtype1_txt",
    "gname"
]

df = df.dropna(subset=required_columns).copy()


# ==========================================
# Page Title
# ==========================================

st.title("🚨 AI Threat Level Prediction")

st.markdown("""
Predict the **threat level** of a terrorist incident using historical patterns from the Global Terrorism Database (GTD).

Select the incident details below and click **Predict Threat Level**.
""")


# ==========================================
# Prediction Form
# ==========================================

with st.form("threat_prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        country = st.selectbox(
            "🌍 Country",
            sorted(df["country_txt"].unique())
        )

        region = st.selectbox(
            "🌎 Region",
            sorted(df["region_txt"].unique())
        )

        attack = st.selectbox(
            "💥 Attack Type",
            sorted(df["attacktype1_txt"].unique())
        )

    with col2:

        weapon = st.selectbox(
            "🔫 Weapon Type",
            sorted(df["weaptype1_txt"].unique())
        )

        target = st.selectbox(
            "🎯 Target Type",
            sorted(df["targtype1_txt"].unique())
        )

        group = st.selectbox(
            "👥 Terrorist Group",
            sorted(df["gname"].unique())
        )

    submitted = st.form_submit_button("🚨 Predict Threat Level")

# ==========================================
# Prediction
# ==========================================

if submitted:

    country_name = country
    region_name = region
    attack_name = attack
    weapon_name = weapon
    target_name = target
    group_name = group

    country, region, attack, weapon, target, group = encode_threat_features(
        encoders,
        country,
        region,
        attack,
        weapon,
        target,
        group
    )

    input_df = {
        "country_txt": [country],
        "region_txt": [region],
        "attacktype1_txt": [attack],
        "weaptype1_txt": [weapon],
        "targtype1_txt": [target],
        "gname": [group]
    }


    input_df = pd.DataFrame(input_df)

    prediction = predict_attack(
        model,
        input_df
    )

    threat_level = decode_prediction(
        target_encoder,
        prediction
    )

    probabilities = prediction_probability(
        model,
        input_df
    )

    confidence = calculate_confidence(
        probabilities
    )

    if threat_level == "LOW":

        st.success(f"🟢 Threat Level : {threat_level}")

    elif threat_level == "MEDIUM":

        st.warning(f"🟡 Threat Level : {threat_level}")

    else:

        st.error(f"🔴 Threat Level : {threat_level}")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)

    st.divider()

    st.subheader("📋 Input Summary")

    display_df = pd.DataFrame({

        "Country": [country_name],
        "Region": [region_name],
        "Attack Type": [attack_name],
        "Weapon Type": [weapon_name],
        "Target Type": [target_name],
        "Terrorist Group": [group_name]

    })

    st.dataframe(
        display_df,
        use_container_width=True
    )