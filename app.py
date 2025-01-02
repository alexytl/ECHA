import streamlit as st
import pandas as pd
from standings_2 import Standings2
from game_reader_2 import GameReader2

def main():
    st.title("ECHA Stats App")
    file = st.file_uploader("Upload CSV File", type="csv")
    if file:
        df = pd.read_csv(file)
        
        game_reader = GameReader2(df)
        game_reader.read_csv(file)
        games = game_reader.get_games()
        teams = game_reader.get_teams()
        standings = Standings2(teams)
        
        st.header("ECHA Standings")
        standings_data = standings.standings()
        standings_df = pd.DataFrame(standings_data)
        st.dataframe(standings_df)
        
if __name__ == "__main__":
    main()
