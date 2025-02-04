import streamlit as st
from game_reader_2 import GameReader2

path = ".devcontainer/dex.csv"

def main():
    st.title("Playoffs")

    game_reader = GameReader2()
    game_reader.read_csv(path)  
    teams = game_reader.get_teams()

    # Debugging: Show teams
    st.write("Teams loaded:", teams)

if __name__ == "__main__":
    main()
