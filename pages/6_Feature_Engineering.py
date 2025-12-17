import streamlit as st
import pandas as pd
import numpy as np

from utils import list_city_files, load_city_data, apply_light_theme

apply_light_theme()

st.title("🧠 Feature Engineering")

# -------------------------------------------------
# Helper Functions (Notebook Logic)
# -------------------------------------------------

def get_indian_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"


def calculate_aqi(row):
    pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
    values = [row[p] for p in pollutants if p in row and pd.notna(row[p])]
    return np.mean(values) if values else np.nan


def aqi_bucket(aqi):
    if pd.isna(aqi):
        return "Unknown"
    elif aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

# -------------------------------------------------
# Dataset Selection
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select City Dataset", files)

df = load_city_data(selected_file)

st.subheader(f"📍 City: {selected_file.replace('_data.csv','')}")

# -------------------------------------------------
# Date Feature Engineering
# -------------------------------------------------
date_cols = [c for c in df.columns if "date" in c.lower()]

if date_cols:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Month_Name"] = df[date_col].dt.month_name()
    df["Season"] = df["Month"].apply(get_indian_season)

st.markdown("### 📅 Date-Based Features Added")
st.dataframe(df[["Year", "Month", "Month_Name", "Season"]].dropna().head())

# -------------------------------------------------
# AQI Feature Engineering
# -------------------------------------------------
st.markdown("---")
st.markdown("### 🌫️ AQI Feature Engineering")

df["AQI"] = df.apply(calculate_aqi, axis=1)
df["AQI_Bucket"] = df["AQI"].apply(aqi_bucket)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### AQI Statistics")
    st.write(df["AQI"].describe())

with col2:
    st.markdown("#### AQI Bucket Distribution")
    st.bar_chart(df["AQI_Bucket"].value_counts())

# -------------------------------------------------
# Missing Value Handling
# -------------------------------------------------
st.markdown("---")
st.markdown("### 🧹 Missing Value Handling")

numeric_cols = df.select_dtypes(include="number").columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

st.success("Missing values in numeric columns filled using mean.")

# -------------------------------------------------
# Correlation-Ready Dataset
# -------------------------------------------------
st.markdown("---")
st.markdown("### 🔗 Correlation-Ready Features")

corr_df = df[numeric_cols]

st.dataframe(corr_df.head())

# -------------------------------------------------
# Final Feature Engineered Dataset
# -------------------------------------------------
st.markdown("---")
st.markdown("### ✅ Final Feature Engineered Dataset")

final_cols = [
    "Year", "Month", "Month_Name", "Season",
    "AQI", "AQI_Bucket"
] + list(numeric_cols)

final_df = df[final_cols].copy()

st.dataframe(final_df.head())

# -------------------------------------------------
# Download Option
# -------------------------------------------------
st.download_button(
    label="⬇️ Download Feature Engineered Dataset",
    data=final_df.to_csv(index=False),
    file_name=f"features_{selected_file}",
    mime="text/csv"
)

st.success("Feature engineering completed successfully.")
