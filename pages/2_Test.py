import pandas as pd
import streamlit as st

try:
    data = pd.read_csv(".devcontainer/dex.csv")
    st.write("CSV loaded successfully!")
    st.write(data.head())  # Show first few rows
except Exception as e:
    st.write(f"Error loading CSV: {e}")
