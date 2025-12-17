import pydeck as pdk

st.markdown("---")
st.markdown("## 🌍 World Map – Pollutant Across All Cities")

show_map = st.checkbox("Show World Map (Select One Pollutant)")

if show_map:

    selected_pollutant = st.selectbox(
        "Select Pollutant to Visualize",
        pollution_cols
    )

    # Load city coordinates
    coord_df = pd.read_csv("city_coordinates.csv")

    map_rows = []

    for file in list_city_files():
        city_name = file.replace("_data.csv", "")

        # Check if city has coordinates
        if city_name not in coord_df["city"].values:
            continue

        city_df = load_city_data(file)

        if selected_pollutant not in city_df.columns:
            continue

        avg_value = city_df[selected_pollutant].mean()

        city_row = coord_df[coord_df["city"] == city_name].iloc[0]

        map_rows.append({
            "city": city_name,
            "lat": city_row["lat"],
            "lon": city_row["lon"],
            "value": avg_value,
        })

    if not map_rows:
        st.warning("No cities found for selected pollutant.")
    else:
        map_df = pd.DataFrame(map_rows)

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=map_df,
            get_position="[lon, lat]",
            get_radius="value * 700",
            get_fill_color=[
                "value < 50 ? 0 : 255",
                "value < 50 ? 180 : 0",
                0,
                160,
            ],
            pickable=True,
        )

        view_state = pdk.ViewState(
            latitude=22,
            longitude=78,
            zoom=4,
        )

        STYLE_MAP = {
            "Light": "carto-positron",
            "Dark": "carto-darkmatter",
            "Voyager": "carto-voyager",
        }

        style = st.selectbox("Select Map Style", list(STYLE_MAP.keys()))

        st.pydeck_chart(
            pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                map_style=STYLE_MAP[style],
                tooltip={
                    "text": "City: {city}\n"
                            + selected_pollutant +
                            ": {value}"
                },
            )
        )

        st.markdown("""
        🟢 **Green** → Lower pollution  
        🔴 **Red** → Higher pollution  
        🔵 **Larger circle** → Higher concentration  
        """)
