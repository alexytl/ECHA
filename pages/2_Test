import streamlit as st
import pandas as pd

path = "../.devcontainer/dex.csv"

# Test reading CSV
try:
    data = pd.read_csv(path)
    st.write("CSV loaded successfully!")
    st.write(data.head())  # Display first few rows of data
except Exception as e:
    st.write(f"Error loading CSV: {e}")
