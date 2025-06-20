# 🌊 Flood Susceptibility Prediction using Elevation & Slope

This project demonstrates a simple, beginner-friendly geospatial machine learning pipeline for predicting flood-prone areas using elevation data and terrain slope. 
It uses PyTorch for modeling and Streamlit for interactive visualization.

🔗 **Live App**: [https://teegardenbee-flood-ml-app.streamlit.app](https://teegardenbee-flood-ml-app.streamlit.app)


## 📌 Project Summary

- 📍 Area of Interest: A region in **Maharashtra, India**
- 🌐 Input Data: **SRTM DEM (30m)** — directly downloaded in code
- 🧠 Model: Basic **PyTorch** neural network classifier
- 🎯 Labels: **Synthetic binary labels** (flood-prone vs safe), based on elevation thresholds
- 📈 Features Used:
  - Elevation (DEM)
  - Slope (calculated from DEM)
- 🌍 Visualization: Streamlit-based web app with selectable map layers


