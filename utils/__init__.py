
import os
import pandas as pd
import streamlit as st

# -------------------------------------------------
# SAFE DATASET PATH (Streamlit Cloud compatible)
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
# GLOBAL LIGHT THEME + DROPDOWN FONT FIX
# -------------------------------------------------
def apply_light_theme():
    st.markdown(
        """
        <style>
        /* ==============================
           APP + SIDEBAR
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
            color: #000000;
        }

        /* ==============================
           SELECTBOX (CLOSED)
           ============================== */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: 1px solid #cccccc !important;
        }

        div[data-baseweb="select"] span {
            color: #000000 !important;
            font-weight: 500;
        }

        /* ==============================
           DROPDOWN LIST (OPEN)
           ============================== */

        /* Keep background dark (Streamlit default) */
        ul[data-baseweb="menu"] {
            background-color: #111827 !important;
        }

        /* FORCE WHITE TEXT FOR ALL OPTIONS */
        ul[data-baseweb="menu"] *,
        li[data-baseweb="menu-item"] * {
            color: #ffffff !important;
            font-weight: 500;
        }

        /* Hovered option */
        ul[data-baseweb="menu"] li:hover {
            background-color: #1f2937 !important;
        }

        /* Selected option */
        li[aria-selected="true"] {
            background-color: #374151 !important;
        }

        /* ==============================
           BUTTONS (NORMAL + DOWNLOAD)
           ============================== */
        div.stButton > button,
        div[data-testid="stDownloadButton"] > button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #cccccc !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
        }

        div.stButton > button:hover,
        div[data-testid="stDownloadButton"] > button:hover {
            background-color: #f2f2f2 !important;
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
           TOP RIGHT ICONS
           ============================== */
        button[data-testid="stToolbarButton"] svg,
        div[data-testid="stToolbar"] svg {
            fill: #000000 !important;
            opacity: 1 !important;
        }

        button[data-testid="stToolbarButton"]:hover svg {
            fill: #2563eb !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
