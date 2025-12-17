import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from utils import list_city_files, load_city_data
from utils import apply_light_theme
apply_light_theme()

st.title("🤖 ML Lab")

# -------------------------------------------------
# Description / Context
# -------------------------------------------------
st.markdown("""
This section demonstrates a **basic machine learning experiment** using the pollution dataset.

- A **regression model** is trained to predict a pollution parameter
- This helps understand **relationships between pollutants**
- The goal is **demonstration**, not production-level modeling
""")

st.markdown("---")

# -------------------------------------------------
# Select Dataset
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select Dataset", files)
df = load_city_data(selected_file)

# -------------------------------------------------
# Select Target & Features
# -------------------------------------------------
numeric_cols = df.select_dtypes(include="number").columns.tolist()

if len(numeric_cols) < 2:
    st.warning("Not enough numeric columns for ML experiment.")
    st.stop()

target = st.selectbox("Select Target Variable (to predict)", numeric_cols)
features = st.multiselect(
    "Select Feature Variables",
    [c for c in numeric_cols if c != target],
    default=[c for c in numeric_cols if c != target][:2]
)

if not features:
    st.info("Please select at least one feature.")
    st.stop()

# -------------------------------------------------
# Prepare Data
# -------------------------------------------------
data = df[features + [target]].dropna()

X = data[features]
y = data[target]

# -------------------------------------------------
# Train Model
# -------------------------------------------------
if st.button("Train Model"):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    st.success("Model trained successfully!")

    st.markdown("### 📊 Model Performance")
    col1, col2 = st.columns(2)
    col1.metric("Mean Absolute Error (MAE)", round(mae, 2))
    col2.metric("R² Score", round(r2, 2))

    st.markdown("### 🔍 Feature Coefficients")
    coef_df = pd.DataFrame({
        "Feature": features,
        "Coefficient": model.coef_
    })
    st.dataframe(coef_df)

st.markdown("""
📝 **Note:**  
This ML Lab is intended to showcase the **workflow of data → features → model → evaluation**.
More advanced models can be added in future work.
""")