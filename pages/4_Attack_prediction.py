import streamlit as st

from utils.loaders import load_dataset, load_attack_prediction_model
from utils.preprocessing import clean_prediction_data, encode_features, prepare_input


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Attack Prediction",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# Load Dataset and Model
# ==========================================

df = load_dataset()

model, feature_encoders, target_encoder = load_attack_prediction_model()


# ==========================================
# Data Preprocessing
# ==========================================

df = clean_prediction_data(df)


# ==========================================
# Page Title
# ==========================================

st.title("🤖 Attack Type Prediction")

st.markdown("""
Predict the **attack type** based on historical terrorism incident information.
Select the incident details below and click **Predict Attack Type**.
""")


# ==========================================
# Prediction Form
# ==========================================

with st.form("prediction_form"):

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

        weapon = st.selectbox(
            "🔫 Weapon Type",
            sorted(df["weaptype1_txt"].unique())
        )

        target = st.selectbox(
            "🎯 Target Type",
            sorted(df["targtype1_txt"].unique())
        )

    with col2:

        group = st.selectbox(
            "👥 Terrorist Group",
            sorted(df["gname"].unique())
        )

        success = st.selectbox(
            "✅ Attack Successful?",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        suicide = st.selectbox(
            "💣 Suicide Attack?",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        nkill = st.number_input(
            "☠ Number of Fatalities",
            min_value=0,
            value=0,
            step=1
        )

        nwound = st.number_input(
            "🏥 Number of Injured",
            min_value=0,
            value=0,
            step=1
        )

    submitted = st.form_submit_button("🚀 Predict Attack Type")

# ==========================================
# Prediction
# ==========================================

if submitted:

    country, region, weapon, target, group = encode_features(
        feature_encoders,
        country,
        region,
        weapon,
        target,
        group
    )

    input_df = prepare_input(
        country,
        region,
        weapon,
        target,
        group,
        success,
        suicide,
        nkill,
        nwound
    )

    prediction = model.predict(input_df)

    attack_type = target_encoder.inverse_transform(prediction)[0]

    probabilities = model.predict_proba(input_df)

    confidence = probabilities.max() * 100

    st.success(f"🎯 Predicted Attack Type: **{attack_type}**")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)

    st.divider()

    st.subheader("📋 Input Summary")

    display_df = input_df.copy()

    display_df["country_txt"] = country
    display_df["region_txt"] = region
    display_df["weaptype1_txt"] = weapon
    display_df["targtype1_txt"] = target
    display_df["gname"] = group

    st.dataframe(
        display_df,
        use_container_width=True
    )