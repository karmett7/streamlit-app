import streamlit as st
import pandas as pd
from utils import list_city_files, load_city_data

st.title("🧠 Feature Engineering")

from utils import apply_light_theme
apply_light_theme()

# -------------------------------------------------
# Description / Context
# -------------------------------------------------
st.markdown("""
This section focuses on **feature engineering**, where new variables are created
from existing data to improve **analysis and modeling performance**.

Common feature engineering steps include:
- Creating **aggregated pollution indicators**
- Extracting **time-based features**
- Normalizing or combining pollutant measures
""")

st.markdown("---")

# -------------------------------------------------
# Select Dataset
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select Dataset", files)

df = load_city_data(selected_file)

# -------------------------------------------------
# Basic Info
# -------------------------------------------------
st.markdown(f"### 📍 Dataset: `{selected_file}`")
st.write("Rows:", df.shape[0], "| Columns:", df.shape[1])

# -------------------------------------------------
# Feature Engineering Options
# -------------------------------------------------
st.markdown("### ⚙️ Create New Features")

numeric_cols = df.select_dtypes(include="number").columns.tolist()

if not numeric_cols:
    st.warning("No numeric columns available for feature engineering.")
    st.stop()

# Option 1: Average Pollution Index
st.markdown("#### 🔹 Average Pollution Index")

if st.button("Create Average Pollution Feature"):
    df["Avg_Pollution"] = df[numeric_cols].mean(axis=1)
    st.success("Feature `Avg_Pollution` created successfully!")
    st.dataframe(df[["Avg_Pollution"]].head())

st.markdown("---")

# Option 2: Date-based features
st.markdown("#### 🔹 Date-Based Features")

date_cols = [c for c in df.columns if "date" in c.lower()]

if date_cols:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    if st.button("Extract Year & Month"):
        df["Year"] = df[date_col].dt.year
        df["Month"] = df[date_col].dt.month
        st.success("Date features `Year` and `Month` created!")
        st.dataframe(df[[date_col, "Year", "Month"]].head())
else:
    st.info("No date column available for time-based feature extraction.")

st.markdown("---")

# -------------------------------------------------
# Preview Engineered Dataset
# -------------------------------------------------
st.markdown("### 👀 Preview Engineered Data")
st.dataframe(df.head())

st.markdown("""
📝 **Note:**  
These engineered features can be used in **EDA**, **Geo-spatial analysis**,  
or as inputs for **machine learning models**.
""")