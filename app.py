import streamlit as st
import folium
from streamlit_folium import st_folium
import os

# ---- Page config ----
st.set_page_config(
    page_title="Flood Prediction",
    layout="wide"
)

# ---- Centered Title ----
st.markdown(
    "<h2 style='text-align: center;'>🌊 Flood Prediction Using Elevation + Slope</h2>",
    unsafe_allow_html=True
)

# ---- Define bounds manually (same as raster bounds) ----
# Example: [[south, west], [north, east]]
# These should match the geospatial extent of your rasters
BOUNDS = [[19.995, 73.70], [20.105, 73.80]]  # Modify if your AOI changes

# ---- Utility to Create Folium Map with PNG Overlay ----
def create_map_with_png_overlay(image_path, label, bounds):
    # Center map on midpoint of bounds
    center_lat = (bounds[0][0] + bounds[1][0]) / 2
    center_lon = (bounds[0][1] + bounds[1][1]) / 2

    fmap = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles='cartodbpositron')

    if os.path.exists(image_path):
        folium.raster_layers.ImageOverlay(
            image=image_path,
            bounds=bounds,
            opacity=0.7,
            name=label,
            interactive=True,
            cross_origin=False,
        ).add_to(fmap)

        folium.LayerControl().add_to(fmap)
    else:
        folium.Marker(
            location=[center_lat, center_lon],
            popup=f"{label} image not found."
        ).add_to(fmap)

    return fmap

# ---- Paths to PNG Images ----
PREDICTED_PATH = "flood_prediction_cleaned.png"
GROUND_TRUTH_PATH = "ground_truth.png"

# ---- Layout: Two Maps Side by Side ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 Predicted Flood Susceptibility")
    pred_map = create_map_with_png_overlay(PREDICTED_PATH, "Predicted", BOUNDS)
    st_folium(pred_map, width=500, height=400)

with col2:
    st.subheader("🟢 Ground Truth Labels")
    gt_map = create_map_with_png_overlay(GROUND_TRUTH_PATH, "Ground Truth", BOUNDS)
    st_folium(gt_map, width=500, height=400)

# ---- Remove Vertical Gaps Using CSS ----
st.markdown("""
    <style>
        /* Remove extra space at bottom */
        .block-container {
            padding-bottom: 0rem !important;
            margin-bottom: 0rem !important;
        }

        /* Reduce space between widgets */
        .element-container {
            margin-bottom: 0rem !important;
        }

        /* Optional: remove white gap in dark mode */
        .main > div {
            padding-bottom: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.caption("Developed by - Atharva Dandagawhal | [@teegardenbee](https://github.com/teegardenbee)")
