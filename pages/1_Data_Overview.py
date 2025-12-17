import streamlit as st
from utils import list_city_files, load_city_data, apply_light_theme

apply_light_theme()

st.title("📂 Data Overview")

# -------------------------------------------------
# Intro / Description
# -------------------------------------------------
st.markdown("""
This section provides an **overview of the urban air pollution datasets** used in this project.

- Each dataset corresponds to **one Indian city**
- Data contains **daily air quality measurements**
- Pollutants include **PM2.5, PM10, NO₂, SO₂, CO, O₃**, etc.
- The datasets are used for **EDA, geo-spatial analysis, and modeling**
""")

st.markdown("---")

# -------------------------------------------------
# Dataset count
# -------------------------------------------------
files = list_city_files()
st.markdown(f"### 📊 Total city datasets: **{len(files)}**")

# -------------------------------------------------
# Dataset preview
# -------------------------------------------------
st.markdown("""
### 🔍 Preview Dataset

Select a city dataset from the dropdown below to:
- Inspect raw pollution records
- Understand feature structure
- Identify missing values and trends
""")

selected_file = st.selectbox("Select City Dataset", files)
df = load_city_data(selected_file)

# -------------------------------------------------
# Display data
# -------------------------------------------------
st.dataframe(df.head())

st.markdown("""
📝 **Note:**  
Only the first few rows are displayed for preview.  
Detailed analysis is available in subsequent sections like **EDA**, **Geo View**, and **City Profiles**.
""")
