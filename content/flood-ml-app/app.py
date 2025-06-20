
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("🌊 Flood Prediction Using Elevation + Slope")

option = st.radio("Choose a map to view:", ["Flood Prediction", "Elevation", "Slope"])

if option == "Flood Prediction":
    st.image("content/flood-ml-app/flood_prediction.png", caption="Predicted Flood Risk", use_container_width=False)
elif option == "Elevation":
    st.image("content/flood-ml-app/elevation_map.png", caption="Elevation Map", use_container_width=False)
elif option == "Slope":
    st.image("content/flood-ml-app/slope_map.png", caption="Slope Map", use_container_width=False)

st.markdown("---")
st.markdown("🛰️ Based on real DEM data and a PyTorch ML model.")
