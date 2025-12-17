import os
import pandas as pd
import streamlit as st

# -------------------------------------------------
# SAFE DATASET PATH (works on Streamlit Cloud)
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

def list_city_files():
    return sorted([
        f for f in os.listdir(DATASET_DIR)
        if f.endswith(".csv")
    ])

def load_city_data(filename):
    return pd.read_csv(os.path.join(DATASET_DIR, filename))

# -------------------------------------------------
# LIGHT THEME + WHITE SELECTBOX FIX
# -------------------------------------------------
def apply_light_theme():
    import streamlit as st

    st.markdown(
        """
        <style>
        /* ==============================
           APP BACKGROUND
           ============================== */
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }

        section[data-testid="stSidebar"] {
            background-color: #f2f2f2;
        }

        /* ==============================
           GENERAL TEXT
           ============================== */
        h1, h2, h3, h4, h5, h6,
        p, span, label, div {
            color: #000000 !important;
        }

        /* ==============================
           SELECTBOX (CLOSED STATE)
           ============================== */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #cccccc !important;
        }

        div[data-baseweb="select"] input {
            color: #000000 !important;
            background-color: #ffffff !important;
        }

        div[data-baseweb="select"] span {
            color: #000000 !important;
        }

        /* ==============================
           DROPDOWN (OPEN STATE)
           ============================== */
        ul[data-baseweb="menu"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #cccccc !important;
        }

        ul[data-baseweb="menu"] li {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        ul[data-baseweb="menu"] li:hover {
            background-color: #e6e6e6 !important;
        }

        /* ==============================
           METRICS
           ============================== */
        div[data-testid="stMetricLabel"],
        div[data-testid="stMetricValue"],
        div[data-testid="stMetricDelta"] {
            color: #000000 !important;
        }

        /* ==============================
           TABLES
           ============================== */
        table, th, td {
            color: #000000 !important;
        }

        /* ==============================
           TOP-RIGHT ICONS
           ============================== */
        button[data-testid="stToolbarButton"] svg,
        div[data-testid="stToolbar"] svg {
            fill: #000000 !important;
            opacity: 1 !important;
        }

        button[data-testid="stToolbarButton"]:hover svg {
            fill: #1f77b4 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
