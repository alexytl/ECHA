import streamlit as st
import pandas as pd
from standings_2 import Standings2
from game_reader_2 import GameReader2

path = ".devcontainer/tank.csv"

def main():
    st.title("ECHA Stats App")
  
    #boring stuff
    game_reader = GameReader2()
    game_reader.read_csv(path)   
    games = game_reader.get_games()
    teams = game_reader.get_teams()
    standings = Standings2(teams)
        
    #standings
    st.header("ECHA Standings")
    standings_data = standings.standings()
    ranked_data = [{"#": rank + 1, **team_data} for rank, 
                       team_data in enumerate(standings_data)]
    standings_df = pd.DataFrame(ranked_data).set_index("#")
    st.dataframe(standings_df)
        
    #rankings
    st.header("Team Rankings")
    stats = ["Strength of Schedule", "Win Percentage", "Points Per Game",
             "Max Points", "Pythagorean Expectation", "GF Per Game", 
             "GA Per Game","GD Per Game"]
    selected = st.selectbox("Rank Teams By: ", stats)
    rank_methods = {"Strength of Schedule": standings.sos_ranked(games), 
                     "Win Percentage": standings.win_pct_ranked(games),
                     "Points Per Game": standings.points_per_ranked(games),
                     "Max Points": standings.max_points_ranked(games),
                     "Pythagorean Expectation": standings.pe_ranked(games),
                     "GF Per Game": standings.gf_per_ranked(games),
                     "GA Per Game": standings.ga_per_ranked(games),
                     "GD Per Game": standings.gd_per_ranked(games)}
    rank_method = rank_methods.get(selected)
    
    if rank_method:
        ranked_data = rank_method(games)
        
        df = pd.DataFrame(
            [{"#": rank + 1, "Team": team, selected: round(value, 3)} 
             for rank, (team, value) in enumerate(ranked_data)]
        ).set_index("#")
        
        st.dataframe(df)
    
if __name__ == "__main__":
    main()
