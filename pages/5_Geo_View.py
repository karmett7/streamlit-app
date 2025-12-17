import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import list_city_files, load_city_data
from utils import apply_light_theme
apply_light_theme()
st.title("🌍 Geo-Spatial Analysis (City Level)")

# Select city dataset
files = list_city_files()
selected_file = st.selectbox("Select City", files)

df = load_city_data(selected_file)

# City name from file
city = selected_file.replace("_data.csv", "")
st.subheader(f"📍 City: {city}")

# Detect pollution columns
pollution_cols = [
    c for c in df.columns
    if c.lower() not in ["date", "year", "month"]
    and df[c].dtype != "object"
]

if not pollution_cols:
    st.warning("No numeric pollution columns found.")
    st.stop()

pollutant = st.selectbox("Select Pollution Parameter", pollution_cols)

# Basic geo-style stats
avg_val = df[pollutant].mean()
max_val = df[pollutant].max()
min_val = df[pollutant].min()

col1, col2, col3 = st.columns(3)
col1.metric("🟢 Min", round(min_val, 2))
col2.metric("🟡 Avg", round(avg_val, 2))
col3.metric("🔴 Max", round(max_val, 2))

st.markdown("---")

# Time-based geo-spatial trend
date_cols = [c for c in df.columns if "date" in c.lower()]

if date_cols:
    date_col = date_cols[0]
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    fig, ax = plt.subplots()

    colors = ["green" if v <= avg_val else "red" for v in df[pollutant]]

    ax.scatter(df[date_col], df[pollutant], c=colors, alpha=0.7)
    ax.axhline(avg_val, color="orange", linestyle="--", label="City Avg")

    ax.set_title(f"{pollutant} Spatial-Temporal Intensity in {city}")
    ax.set_xlabel("Time")
    ax.set_ylabel(pollutant)
    ax.legend()

    st.pyplot(fig)
else:
    st.info("No date column available for temporal geo analysis.")

st.markdown("""
### 🗺️ Geo-Spatial Interpretation
- 🟢 Green points indicate **low pollution zones (time periods)**
- 🔴 Red points indicate **high pollution intensity**
- 🟠 Dashed line shows **city average pollution**
""")

# =================================================
# OPTIONAL: World Map – One Pollutant Across Cities
# =================================================
import pydeck as pdk

st.markdown("---")
st.markdown("## 🌍 World Map – Pollutant Across Cities")

show_map = st.checkbox("Show World Map (Select One Pollutant)")

if show_map:

    # City coordinates
    CITY_COORDS = {
    "Ahmedabad": (23.0225, 72.5714),
    "Aizawl": (23.7271, 92.7176),
    "Amaravati": (16.5730, 80.3575),
    "Amritsar": (31.6340, 74.8723),
    "Bengaluru": (12.9716, 77.5946),
    "Bhopal": (23.2599, 77.4126),
    "Brajrajnagar": (21.8200, 83.9230),
    "Chandigarh": (30.7333, 76.7794),
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Delhi": (28.6139, 77.2090),
    "Ernakulam": (9.9816, 76.2999),
    "Gurugram": (28.4595, 77.0266),
    "Hyderabad": (17.3850, 78.4867),
    "Jaipur": (26.9124, 75.7873),
    "Kolkata": (22.5726, 88.3639),
    "Lucknow": (26.8467, 80.9462),
    "Mumbai": (19.0760, 72.8777),
    "Patna": (25.5941, 85.1376),
    "Pune": (18.5204, 73.8567),
    "Visakhapatnam": (17.6868, 83.2185),
    "Guwahati": (26.1445, 91.7362),
    "Jorapokhar": (23.7500, 86.4000),
    "Talcher": (20.9500, 85.2300),
    "Shillong": (25.5788, 91.8933),
    "Bengaluru": (12.9716, 77.5946)
}


    # Pollutant selection
    selected_pollutant = st.selectbox(
        "Select Pollutant to Visualize",
        pollution_cols
    )

    map_rows = []

    for file in list_city_files():
        city_name = file.replace("_data.csv", "")

        if city_name not in CITY_COORDS:
            continue

        city_df = load_city_data(file)

        if selected_pollutant not in city_df.columns:
            continue

        avg_value = city_df[selected_pollutant].mean()

        lat, lon = CITY_COORDS[city_name]

        map_rows.append({
            "city": city_name,
            "lat": lat,
            "lon": lon,
            "value": avg_value,
        })

    if not map_rows:
        st.warning("No data available for selected pollutant.")
    else:
        map_df = pd.DataFrame(map_rows)

        # Color scale: green → red
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=map_df,
            get_position="[lon, lat]",
            get_radius="value * 800",
            get_fill_color=[
                "value < 50 ? 0 : 255",
                "value < 50 ? 200 : 0",
                0,
                160,
            ],
            pickable=True,
        )

        view_state = pdk.ViewState(
            latitude=22.0,
            longitude=78.0,
            zoom=4,
        )

        STYLE_MAP = {
            "Light": pdk.map_styles.LIGHT,
            "Dark": pdk.map_styles.DARK,
        }

        style_name = st.selectbox("Select Map Style", list(STYLE_MAP.keys()))

        st.pydeck_chart(
            pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                map_style=STYLE_MAP[style_name],
                tooltip={
                    "text": "City: {city}\nPollutant: "
                            + selected_pollutant +
                            "\nAvg Value: {value}"
                },
            )
        )

        st.markdown("""
        🟢 **Green** → Lower pollution  
        🔴 **Red** → Higher pollution  
        🔵 **Larger circle** → Higher concentration  
        """)
