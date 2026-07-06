import streamlit as st

from utils.loaders import load_attack_prediction_model
from utils.preprocessing import  encode_features, prepare_input


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Attack Prediction",
    page_icon="🤖",
    layout="wide"
)



model, feature_encoders, target_encoder = load_attack_prediction_model()


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
            sorted(feature_encoders["country_txt"].classes_)
)

        region = st.selectbox(
            "🌎 Region",
            sorted(feature_encoders["region_txt"].classes_)
        )

        weapon = st.selectbox(
            "🔫 Weapon Type",
            sorted(feature_encoders["weaptype1_txt"].classes_)
        )

        target = st.selectbox(
            "🎯 Target Type",
            sorted(feature_encoders["targtype1_txt"].classes_)
        )

    with col2:

        group = st.selectbox(
            "👥 Terrorist Group",
            sorted(feature_encoders["gname"].classes_)
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

    country_name = country
    region_name = region
    weapon_name = weapon
    target_name = target
    group_name = group

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

    display_df["country_txt"] = country_name
    display_df["region_txt"] = region_name
    display_df["weaptype1_txt"] = weapon_name
    display_df["targtype1_txt"] = target_name
    display_df["gname"] = group_name
    st.dataframe(
        display_df,
        use_container_width=True
    )