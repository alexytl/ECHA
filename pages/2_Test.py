import os
import streamlit as st

# Log the current working directory to Streamlit
st.write("Current working directory:", os.getcwd())

# Then construct your file path
path = os.path.join(os.getcwd(), ".devcontainer", "dex.csv")
