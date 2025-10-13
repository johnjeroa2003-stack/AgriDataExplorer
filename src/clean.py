# src/clean.py
"""
AgriData Explorer - Data Cleaning Script
----------------------------------------
This script cleans the ICRISAT District-Level dataset.
It standardizes units, fixes column names, handles missing values,
and exports the cleaned dataset for analysis.

Author: Johnson Jerald
"""

import pandas as pd
import numpy as np
from pathlib import Path

# --- File Paths ---
DATA_PATH = Path("../data/ICRISAT_District_Data.csv")
OUTPUT_PATH = Path("../results/cleaned_data.csv")

def load_icrisat(file_path: Path) -> pd.DataFrame:
    """Load the ICRISAT dataset."""
    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names."""
    df.columns = (
        df.columns.str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[()/%]", "", regex=True)
        .str.lower()
    )
    return df

def convert_units(df: pd.DataFrame) -> pd.DataFrame:
    """Convert units like '000 ha' → ha and '000 tons' → tons."""
    for col in df.columns:
        if "000_ha" in col:
            df[col] = df[col] * 1000
        elif "000_tons" in col or "000_tonnes" in col:
            df[col] = df[col] * 1000
    return df

def clean_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Convert numeric columns and handle errors."""
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values."""
    missing = df.isna().sum().sum()
    if missing > 0:
        print(f"⚠️ Found {missing} missing values. Filling with zeros.")
        df = df.fillna(0)
    return df

def save_cleaned(df: pd.DataFrame, output_path: Path):
    """Save cleaned data to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"💾 Cleaned data saved to: {output_path}")

def clean_all():
    """Full cleaning pipeline."""
    df = load_icrisat(DATA_PATH)
    df = clean_columns(df)
    df = convert_units(df)
    df = clean_numeric(df)
    df = handle_missing(df)
    save_cleaned(df, OUTPUT_PATH)
    print("🎯 Cleaning complete!")

if __name__ == "__main__":
    clean_all()
