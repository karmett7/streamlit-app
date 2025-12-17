import streamlit as st
from utils import apply_light_theme


# MUST BE FIRST (NO CODE ABOVE THIS)

st.set_page_config(
    page_title="Urban Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Apply Global Light Theme

apply_light_theme()

# Home Page Background Image (HOME ONLY)

def apply_home_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                rgba(255,255,255,0.85),
                rgba(255,255,255,0.85)
            ),
            url("assets/bg.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_home_background()

# Page Content

st.title("📊 Urban Data Analysis Dashboard")

st.markdown(
    "Welcome to the **Urban Data Analysis App**, an interactive dashboard designed to "
    "analyze **air pollution trends across major Indian cities**.\n\n"
    "This application provides insights into **pollutant concentration levels**, "
    "**data quality**, **spatial trends**, and **basic machine learning experiments**."
)

st.markdown("---")


# Cities Covered

st.markdown("## 🏙️ Cities Covered")

st.markdown(
    "The dataset includes air quality data from **26 major Indian cities**, such as:\n\n"
    "- Ahmedabad\n"
    "- Bengaluru\n"
    "- Chennai\n"
    "- Delhi\n"
    "- Gurugram\n"
    "- Bhopal\n"
    "- Amritsar\n"
    "- Chandigarh\n"
    "- Coimbatore\n"
    "- Ernakulam\n\n"
    "*(and other metropolitan and urban regions)*\n\n"
    "Each city has a **separate dataset** containing daily pollution measurements "
    "collected over multiple years."
)

st.markdown("---")

# Pollutants Explained

st.markdown("## 🌫️ Pollutants Analyzed")

st.markdown(
    "- **PM2.5** – Fine particulate matter (high health risk)\n"
    "- **PM10** – Coarse particulate matter\n"
    "- **NO (Nitric Oxide)** – Vehicle and industrial emissions\n"
    "- **NO₂ (Nitrogen Dioxide)** – Causes respiratory problems\n"
    "- **NOx** – Combined nitrogen oxides\n"
    "- **NH₃ (Ammonia)** – Agricultural and industrial emissions\n"
    "- **CO (Carbon Monoxide)** – Incomplete fuel combustion\n"
    "- **SO₂ (Sulfur Dioxide)** – Power plants and industrial sources\n"
    "- **O₃ (Ozone)** – Secondary atmospheric pollutant\n"
    "- **Benzene / Toluene** – Volatile organic compounds (VOCs)\n\n"
    "These pollutants are used to study **air quality trends**, "
    "**health impact**, and **urban environmental conditions**."
)

st.markdown("---")

st.success("👉 Use the sidebar to navigate through different sections of the app.")
