import streamlit as st
import pandas as pd
import joblib

from utils.constants import (
    DATASET_PATH,
    ATTACK_MODEL_PATH,
    FEATURE_ENCODER_PATH,
    TARGET_ENCODER_PATH
)


# ==========================================
# Dataset Loader
# ==========================================

@st.cache_data(show_spinner=False)
def load_dataset():

    df = pd.read_csv(
        DATASET_PATH,
        encoding="latin1",
        low_memory=False
    )

    return df


# ==========================================
# Attack Prediction Model
# ==========================================

@st.cache_resource(show_spinner=False)
def load_attack_prediction_model():

    model = joblib.load(
        'models/attack_prediction_model.pkl'
    )

    feature_encoders = joblib.load(
        "models/feature_encoders.pkl"
    )

    target_encoder = joblib.load(
        "models/target_encoder.pkl"
    )

    return model, feature_encoders, target_encoder


# ==========================================
# Threat Level Prediction Model
# ==========================================

@st.cache_resource(show_spinner=False)
def load_threat_prediction_model():

    model = joblib.load(
        "models/threat_level_model.pkl"
    )

    feature_encoders = joblib.load(
        "models/threat_feature_encoders.pkl"
    )

    target_encoder = joblib.load(
        "models/threat_target_encoder.pkl"
    )

    return model, feature_encoders, target_encoder