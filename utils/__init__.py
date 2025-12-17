import os
import pandas as pd
import streamlit as st

DATASET_DIR = "dataset"

def list_city_files():
    return sorted([
        f for f in os.listdir(DATASET_DIR)
        if f.endswith(".csv")
    ])

def load_city_data(filename):
    return pd.read_csv(os.path.join(DATASET_DIR, filename))

def apply_light_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }

        section[data-testid="stSidebar"] {
            background-color: #f2f2f2;
        }

        h1, h2, h3, h4, h5, h6,
        p, span, label, div {
            color: #000000 !important;
        }

        div[data-testid="stMetricLabel"],
        div[data-testid="stMetricValue"],
        div[data-testid="stMetricDelta"] {
            color: #000000 !important;
        }

        table, th, td {
            color: #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
