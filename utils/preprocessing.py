import pandas as pd


# ==========================================
# Remove Missing Values
# ==========================================

def clean_prediction_data(df):

    df = df.dropna(
        subset=[
            "country_txt",
            "region_txt",
            "weaptype1_txt",
            "targtype1_txt",
            "gname"
        ]
    )

    return df


# ==========================================
# Encode Features
# ==========================================

def encode_features(encoders, country, region, weapon, target, group):

    country = encoders["country_txt"].transform([country])[0]

    region = encoders["region_txt"].transform([region])[0]

    weapon = encoders["weaptype1_txt"].transform([weapon])[0]

    target = encoders["targtype1_txt"].transform([target])[0]

    group = encoders["gname"].transform([group])[0]

    return country, region, weapon, target, group


# ==========================================
# Prepare Input
# ==========================================

def prepare_input(country, region, weapon, target, group, success, suicide, nkill, nwound):

    input_df = pd.DataFrame({

        "country_txt": [country],

        "region_txt": [region],

        "weaptype1_txt": [weapon],

        "targtype1_txt": [target],

        "gname": [group],

        "success": [success],

        "suicide": [suicide],

        "nkill": [nkill],

        "nwound": [nwound]

    })

    return input_df

# ==========================================
# Encode Threat Features
# ==========================================

def encode_threat_features(encoders, country, region, attack, weapon, target, group):

    country = encoders["country_txt"].transform([country])[0]
    region = encoders["region_txt"].transform([region])[0]
    attack = encoders["attacktype1_txt"].transform([attack])[0]
    weapon = encoders["weaptype1_txt"].transform([weapon])[0]
    target = encoders["targtype1_txt"].transform([target])[0]
    group = encoders["gname"].transform([group])[0]

    return country, region, attack, weapon, target, group