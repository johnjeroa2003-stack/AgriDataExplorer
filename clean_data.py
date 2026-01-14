import pandas as pd
import numpy as np

# Load raw dataset
input_path = "data/raw/icrisat_raw.csv"
df = pd.read_csv(input_path)

print("Raw data loaded")
print("Shape:", df.shape)

# -----------------------------
# Standardize column names
# -----------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
)

# -----------------------------
# Handle missing values
# -----------------------------
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

df = df.fillna("Unknown")

# -----------------------------
# Data type corrections
# -----------------------------
df["year"] = df["year"].astype(int)

# -----------------------------
# Remove duplicate rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Save cleaned dataset
# -----------------------------
output_path = "data/cleaned/agriculture_cleaned.csv"
df.to_csv(output_path, index=False)

print("Data cleaning completed")
print("Cleaned data shape:", df.shape)
