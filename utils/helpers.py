import pandas as pd


# ==========================================
# Format Numbers
# ==========================================

def format_number(number):

    return f"{number:,}"


# ==========================================
# Convert DataFrame to CSV
# ==========================================

def dataframe_to_csv(df):

    return df.to_csv(index=False).encode("utf-8")


# ==========================================
# Calculate Prediction Confidence
# ==========================================

def calculate_confidence(probabilities):

    return probabilities.max() * 100


# ==========================================
# Safe Sum
# ==========================================

def safe_sum(series):

    return int(series.fillna(0).sum())


# ==========================================
# Top Records
# ==========================================

def top_records(df, column, count=10):

    return (
        df.groupby(column)
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(count)
    )