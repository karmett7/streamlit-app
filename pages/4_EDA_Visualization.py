import streamlit as st
import matplotlib.pyplot as plt
from utils import list_city_files, load_city_data
from utils import apply_light_theme
apply_light_theme()
st.title("📈 EDA Visualization (High vs Low Pollution)")

files = list_city_files()
selected_file = st.selectbox("Select City Dataset", files)

df = load_city_data(selected_file)

num_cols = df.select_dtypes(include="number").columns

col = st.selectbox("Select Pollution Column", num_cols)

# Threshold (median)
threshold = df[col].median()

low = df[df[col] <= threshold][col]
high = df[df[col] > threshold][col]

fig, ax = plt.subplots()

ax.hist(low, bins=30, color="green", alpha=0.6, label="Low Pollution")
ax.hist(high, bins=30, color="red", alpha=0.6, label="High Pollution")

ax.set_title(f"{col} – Low vs High Pollution")
ax.set_xlabel(col)
ax.set_ylabel("Frequency")
ax.legend()

st.pyplot(fig)