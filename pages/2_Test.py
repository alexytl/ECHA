import streamlit as st
from game_reader_2 import GameReader2

path = ".devcontainer/dex.csv"

def main():
    st.title("Playoffs")

    game_reader = GameReader2()
    game_reader.read_csv(path)  
    teams = game_reader.get_teams()

    # Debugging: Show teams with attributes
    st.write("Teams loaded:")

    for team in teams:
        st.write({
            "Name": team.get_name(),
            "Points": team.get_points(),
            "Games Played": team.get_gp(),
            "Goal Difference": team.get_gd(),
            "Max Points": team.get_max_points()
        })

if __name__ == "__main__":
    main()
