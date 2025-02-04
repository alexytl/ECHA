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
            st.write(f"Team Name: {team.get_name()}")  # Ensure this method works in Team class
            st.write(f"Team Wins: {team.get_wins()}")
            st.write(f"Team Losses: {team.get_losses()}")
    else:
        st.warning("No teams found. Something went wrong with loading data.")

    # Debug: Check if games are correctly loaded
    games = game_reader.get_games()
    st.write(f"Games loaded: {games}")

    # Create Standings based on loaded teams
    standings_data = [{"Team": team.get_name(), "Wins": team.get_wins()} for team in teams]
    standings_df = pd.DataFrame(standings_data)

    # Display the standings table
    st.header("Standings")
    st.dataframe(standings_df)

    # Debugging Rankings (Sorting teams by Wins)
    sorted_teams = sorted(standings_data, key=lambda x: x["Wins"], reverse=True)
    sorted_teams_df = pd.DataFrame(sorted_teams).set_index("Team")
    st.header("Ranked Teams")
    st.dataframe(sorted_teams_df)

    # Debug: Check if plotting is working (simple bar plot of Wins)
    if teams:
        team_names = [team.get_name() for team in teams]
        wins = [team.get_wins() for team in teams]
        
        fig, ax = plt.subplots()
        ax.bar(team_names, wins)
        ax.set_xlabel("Team")
        ax.set_ylabel("Wins")
        ax.set_title("Wins per Team")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
