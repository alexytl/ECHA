import os
import streamlit as st

try:
    with open(".devcontainer/dex.csv", 'r', encoding='utf-8') as file:
        st.write("File is accessible!")
except Exception as e:
    st.write(f"Error opening file: {e}")
