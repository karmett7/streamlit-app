import streamlit as st
from utils import list_city_files, load_city_data

st.title("❌ Missing Values Analysis")
from utils import apply_light_theme
apply_light_theme()

# -------------------------------------------------
# Description / Context
# -------------------------------------------------
st.markdown("""
This section analyzes **missing values** in the selected city dataset.

- Missing values may occur due to **sensor failures**, **data collection issues**, or **reporting gaps**
- Understanding missing data is important before **EDA, feature engineering, and modeling**
- Columns with high missing values may require **imputation or exclusion**
""")

st.markdown("---")

# -------------------------------------------------
# Select dataset
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select Dataset", files)

df = load_city_data(selected_file)

# -------------------------------------------------
# Missing values computation
# -------------------------------------------------
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100

missing_df = (
    missing_count
    .to_frame(name="Missing Count")
    .assign(Missing_Percentage=missing_percent.round(2))
)

# -------------------------------------------------
# Display results
# -------------------------------------------------
st.markdown("### 📊 Missing Values Summary")

st.dataframe(missing_df)

st.markdown("""
📝 **Interpretation Guide:**
- **0% missing** → Complete and reliable column  
- **< 10% missing** → Can be handled with simple imputation  
- **> 30% missing** → Requires careful handling or exclusion  
""")