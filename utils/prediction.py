# ==========================================
# Attack Prediction
# ==========================================

def predict_attack(model, input_df):

    prediction = model.predict(input_df)

    return prediction


# ==========================================
# Prediction Confidence
# ==========================================

def prediction_probability(model, input_df):

    probability = model.predict_proba(input_df)

    return probability


# ==========================================
# Decode Prediction
# ==========================================

def decode_prediction(target_encoder, prediction):

    attack_type = target_encoder.inverse_transform(prediction)[0]

    return attack_type