import streamlit as st
import pandas as pd
import folium

st.title("Excel Update App")

df = pd.read_csv("suplocation.csv")
st.write(df)


# Show/Hide the map button
if "map_state" not in st.session_state:
    st.session_state.map_state = False

if st.button("Show/Hide Map"):
    st.session_state.map_state = not st.session_state.map_state

# Display the map when the button is clicked and map_state is True
if st.session_state.map_state:
    # Display the map
    st.header("Map with Colorful Pins")
    m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=5, tiles="openstreetmap")

    # Define a color palette for the markers
    color_palette = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928']

    for index, row in df.iterrows():
        tooltip = f"{row['name']}"
        color = color_palette[index % len(color_palette)]  # Cycle through the colors
        folium.Marker([row['latitude'], row['longitude']], tooltip=tooltip, icon=folium.Icon(color=color)).add_to(m)

    # Add some map styling
    folium.TileLayer("cartodbdark_matter").add_to(m)
    folium.TileLayer("cartodbpositron").add_to(m)
    folium.TileLayer("openstreetmap").add_to(m)
    folium.TileLayer("stamentoner").add_to(m)
    folium.TileLayer("stamenterrain").add_to(m)
    folium.TileLayer("stamenwatercolor").add_to(m)


    folium.LayerControl().add_to(m)

    # Render the map as an HTML iframe
    map_html = m.get_root().render()
    st.components.v1.html(map_html, height=500)
