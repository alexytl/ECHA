import streamlit as st
from game_reader_2 import GameReader2
from team import Team

path = ".devcontainer/dex.csv"

def main():
    st.title("Playoffs")

    game_reader = GameReader2()
    game_reader.read_csv(path)  
    teams = game_reader.get_teams()

    st.write("Teams loaded:")

    if teams:
        first_team = teams[0]
        st.write("First Team Object:", first_team)
        st.write("Available Attributes & Methods:", dir(first_team))

if __name__ == "__main__":
    main()
