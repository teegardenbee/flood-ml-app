import streamlit as st
import folium
import rasterio
from rasterio.plot import reshape_as_image
from streamlit_folium import st_folium
import numpy as np
import branca.colormap as cm
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

# ---- Utility to Create Folium Map with Raster Overlay ----
def create_map_with_raster(raster_path, label):
    with rasterio.open(raster_path) as src:
        bounds = src.bounds
        array = src.read(1)
        transform = src.transform

    # Normalize to 0–1
    array = np.nan_to_num(array)
    min_val, max_val = array.min(), array.max()
    norm = (array - min_val) / (max_val - min_val + 1e-6)

    # Create colormap
    colormap = cm.linear.Blues_09.scale(0, 1) if "predicted" in raster_path.lower() else cm.linear.Greens_09.scale(0, 1)
    colormap.caption = label

    # Create folium map centered on raster
    center_lat = (bounds.top + bounds.bottom) / 2
    center_lon = (bounds.left + bounds.right) / 2
    fmap = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles='cartodbpositron')

    # Add raster layer
    folium.raster_layers.ImageOverlay(
        image=norm,
        bounds=[[bounds.bottom, bounds.left], [bounds.top, bounds.right]],
        colormap=lambda x: colormap(x),
        opacity=0.8,
        name=label,
    ).add_to(fmap)

    # Add layer control and colormap
    colormap.add_to(fmap)
    folium.LayerControl().add_to(fmap)

    return fmap

# ---- Paths to Rasters ----
PREDICTED_PATH = "flood_prediction.tif"
GROUND_TRUTH_PATH = "ground_truth.tif"  # make sure this exists

# ---- Layout: Two Maps Side by Side ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 Predicted Flood Susceptibility")
    pred_map = create_map_with_raster(PREDICTED_PATH, "Predicted")
    st_folium(pred_map, width=500, height=400)

with col2:
    st.subheader("🟢 Ground Truth Labels")
    gt_map = create_map_with_raster(GROUND_TRUTH_PATH, "Ground Truth")
    st_folium(gt_map, width=500, height=400)

# ---- Footer ----
st.markdown("---")
st.caption("Developed by [@teegardenbee](https://github.com/teegardenbee)")
