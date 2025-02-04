import streamlit as st
from game_reader_2 import GameReader2
from team import Team  # Adjust if necessary

path = ".devcontainer/dex.csv"

def main():
    st.title("Playoffs")

    game_reader = GameReader2()
    game_reader.read_csv(path)  
    teams = game_reader.get_teams()

    # Check if teams list is empty
    st.write("Number of teams:", len(teams))

    if teams:
        first_team = teams[0]
        st.write("Type of first team object:", type(first_team))  # Check type
        st.write("First Team Object:", first_team)
        st.write("Available Attributes & Methods:", dir(first_team))
    else:
        st.write("No teams loaded.")

if __name__ == "__main__":
    main()
