import os
import streamlit as st

path = ".devcontainer/dex.csv"
file_exists = os.path.exists(path)

st.write(f"Does the file exist? {file_exists}")
