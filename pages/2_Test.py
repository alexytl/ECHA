import streamlit as st
import pandas as pd
from game_reader_2 import GameReader2
from team import Team  # Assuming Team is defined in your team.py file

# Define a path to the file for testing purposes
path = ".devcontainer/dex.csv"  # Adjust as needed

def main():
    st.title("Playoffs Simulation - Debugging")

    # Debug: Check current working directory
    st.write(f"Current working directory: {os.getcwd()}")

    # Initialize GameReader2 and load data
    game_reader = GameReader2()

    # Debug: Check if the game_reader object is created
    st.write(f"GameReader2 object: {game_reader}")

    try:
        game_reader.read_csv(path)  # Try reading the CSV
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return

    # Debug: Check if the teams are correctly loaded
    teams = game_reader.get_teams()
    st.write(f"Teams loaded: {teams}")

    # Test if we have teams and they are valid objects (Team class should be well-defined)
    if teams:
        for team in teams:
            st.write(f"Team Name: 
