import streamlit as st
import pandas as pd
import requests
from urllib.parse import quote
from utils import list_city_files, load_city_data

from utils import apply_light_theme
apply_light_theme()

# -------------------------------------------------
# PAGE TITLE
# -------------------------------------------------
st.title("🏙️ City Profiles")

# -------------------------------------------------
# Wikipedia city name normalization
# -------------------------------------------------
WIKI_CITY_MAP = {
    "Gurugram": "Gurgaon",
    "Bengaluru": "Bangalore",
    "Brajrajnagar": "Brajrajnagar Odisha",
}

# -------------------------------------------------
# Select City Dataset
# -------------------------------------------------
files = list_city_files()
selected_file = st.selectbox("Select City", files)

df = load_city_data(selected_file)

city = selected_file.replace("_data.csv", "")
wiki_city = WIKI_CITY_MAP.get(city, city)

st.header(city)

# -------------------------------------------------
# Wikipedia Fetch (with fallback)
# -------------------------------------------------
def fetch_wikipedia(city_name):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(city_name)}"
        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            data = r.json()
            return (
                data.get("extract"),
                data.get("thumbnail", {}).get("source"),
                data.get("content_urls", {}).get("desktop", {}).get("page"),
            )
    except Exception:
        pass

    # Fallback (always works)
    fallback_link = f"https://en.wikipedia.org/wiki/{quote(city_name)}"
    return (
        f"{city_name} is a major city in India. Detailed information is available on Wikipedia.",
        None,
        fallback_link,
    )

summary, image_url, wiki_link = fetch_wikipedia(wiki_city)

# -------------------------------------------------
# Layout: Overview + Image
# -------------------------------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("🧾 City Overview")
    st.write(summary)
    if wiki_link:
        st.markdown(f"[🔗 Read more on Wikipedia]({wiki_link})")

with right:
    if image_url:
        st.image(image_url, caption=city, use_column_width=True)

st.markdown("---")

# -------------------------------------------------
# Dataset Statistics
# -------------------------------------------------
st.subheader("📊 Dataset Statistics")

c1, c2, c3 = st.columns(3)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing Values", int(df.isnull().sum().sum()))

# -------------------------------------------------
# Numerical Summary
# -------------------------------------------------
st.subheader("📈 Numerical Summary")
st.dataframe(df.describe())