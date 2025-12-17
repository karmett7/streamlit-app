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
# GLOBAL LIGHT THEME + COMPLETE UI FIX
# -------------------------------------------------
def apply_light_theme():
    st.markdown(
        """
        <style>
        /* Force light theme everywhere */
        :root {
            color-scheme: light;
        }

        .stApp {
            background-color: #ffffff;
            color: #000000;
        }

        section[data-testid="stSidebar"] {
            background-color: #f2f2f2;
        }

        /* Text */
        * {
            color: #000000 !important;
        }

        /* Selectbox closed */
        div[data-baseweb="select"] {
            background-color: #ffffff !important;
        }

        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: 1px solid #cccccc !important;
        }

        /* Dropdown popup */
        div[data-baseweb="popover"] {
            background-color: #ffffff !important;
        }

        /* Dropdown list */
        ul[data-baseweb="menu"] {
            background-color: #ffffff !important;
        }

        /* Each option */
        ul[data-baseweb="menu"] li {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* Hover */
        ul[data-baseweb="menu"] li:hover {
            background-color: #e6e6e6 !important;
        }

        /* Selected */
        ul[data-baseweb="menu"] li[aria-selected="true"] {
            background-color: #d9d9d9 !important;
        }

        /* Buttons */
        button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #cccccc !important;
        }

        button:hover {
            background-color: #f2f2f2 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

