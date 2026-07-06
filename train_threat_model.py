import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# ---------------------------------------------------
# Create models folder
# ---------------------------------------------------

os.makedirs("models", exist_ok=True)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

print("Loading GTD Dataset...")

df = pd.read_csv(
    "data/globalterrorism.csv",
    encoding="latin1",
    low_memory=False
)

print(df.shape)

# ---------------------------------------------------
# Features
# ---------------------------------------------------

features = [

    "country_txt",
    "region_txt",
    "attacktype1_txt",
    "weaptype1_txt",
    "targtype1_txt",
    "gname"

]

target = "threat_level"

required_columns = features + ["nkill", "nwound"]

df = df[required_columns]

# ---------------------------------------------------
# Remove Missing Values
# ---------------------------------------------------

df = df.dropna().copy()

print("After Cleaning:", df.shape)

# ---------------------------------------------------
# Create Threat Level
# ---------------------------------------------------

df["impact"] = df["nkill"] + df["nwound"]


def classify_threat(impact):

    if impact <= 2:
        return "LOW"

    elif impact <= 10:
        return "MEDIUM"

    else:
        return "HIGH"


df[target] = df["impact"].apply(classify_threat)

# ---------------------------------------------------
# Threat Level Distribution
# ---------------------------------------------------

print()

print("=" * 50)

print("Threat Level Distribution")

print("=" * 50)

print(df[target].value_counts())

# ---------------------------------------------------
# Remove Leakage Columns
# ---------------------------------------------------

df = df.drop(columns=["nkill", "nwound", "impact"])

# ---------------------------------------------------
# Encode Features
# ---------------------------------------------------

encoders = {}

for col in features:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

# ---------------------------------------------------
# Encode Target
# ---------------------------------------------------

target_encoder = LabelEncoder()

df[target] = target_encoder.fit_transform(df[target])

# ---------------------------------------------------
# Features / Labels
# ---------------------------------------------------

X = df[features]

y = df[target]

# ---------------------------------------------------
# Train/Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y

)

# ---------------------------------------------------
# Train Random Forest
# ---------------------------------------------------

print()

print("=" * 50)

print("Training Threat Level Model...")

print("=" * 50)

model = RandomForestClassifier(

    n_estimators=300,
    random_state=42,
    n_jobs=-1

)

model.fit(

    X_train,
    y_train

)

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

pred = model.predict(

    X_test

)

# ---------------------------------------------------
# Accuracy
# ---------------------------------------------------

accuracy = accuracy_score(

    y_test,
    pred

)

print()

print("=" * 50)

print("Accuracy")

print("=" * 50)

print(accuracy)

print()

print("=" * 50)

print("Classification Report")

print("=" * 50)

print(

    classification_report(

        y_test,
        pred

    )

)

print("=" * 50)

print("Confusion Matrix")

print("=" * 50)

print(

    confusion_matrix(

        y_test,
        pred

    )

)

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

joblib.dump(

    model,
    "models/threat_level_model.pkl"

)

joblib.dump(

    encoders,
    "models/threat_feature_encoders.pkl"

)

joblib.dump(

    target_encoder,
    "models/threat_target_encoder.pkl"

)

print()

print("=" * 50)

print("Threat Level Model Saved Successfully")

print("=" * 50)