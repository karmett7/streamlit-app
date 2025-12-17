
import streamlit as st
import pandas as pd
from utils import list_city_files, load_city_data

from utils import apply_light_theme
apply_light_theme()

st.title("⬇️ Downloads")

# -------------------------------------------------
# Description
# -------------------------------------------------
st.markdown("""
This section allows users to download datasets in **different processing stages**.

### Available Downloads:
- **Original Dataset** – Raw city-wise pollution data
- **Cleaned Dataset** – Missing values handled
- **ML Dataset** – Model-ready numerical features
""")

st.markdown("---")

# -------------------------------------------------
# Select Dataset
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select Dataset to Download", files)

df = load_city_data(selected_file)

# -------------------------------------------------
# 1️⃣ Original Dataset Download
# -------------------------------------------------
st.markdown("## 📁 Original Dataset")

st.download_button(
    label="⬇️ Download Original CSV",
    data=df.to_csv(index=False),
    file_name=selected_file,
    mime="text/csv"
)

# -------------------------------------------------
# 2️⃣ Cleaned Dataset
# -------------------------------------------------
st.markdown("## 🧹 Cleaned Dataset")

st.markdown("""
Cleaning steps applied:
- Numerical columns → missing values filled using **mean**
- Categorical columns → missing values filled using **mode**
""")

cleaned_df = df.copy()

for col in cleaned_df.columns:
    if cleaned_df[col].dtype != "object":
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())
    else:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mode()[0])

st.download_button(
    label="⬇️ Download Cleaned Dataset",
    data=cleaned_df.to_csv(index=False),
    file_name=f"cleaned_{selected_file}",
    mime="text/csv"
)

# -------------------------------------------------
# 3️⃣ ML-ready Dataset
# -------------------------------------------------
st.markdown("## 🤖 ML-Ready Dataset")

st.markdown("""
ML Dataset includes:
- Only **numerical pollution features**
- Missing values handled
- Ready for **regression or classification**
""")

ml_df = cleaned_df.select_dtypes(include="number")

st.download_button(
    label="⬇️ Download ML Dataset",
    data=ml_df.to_csv(index=False),
    file_name=f"ml_{selected_file}",
    mime="text/csv"
)

st.markdown("""
📝 **Note:**  
The ML dataset can be directly used in the **ML Lab** or external machine learning workflows.
""")