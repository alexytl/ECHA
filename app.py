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
    rank_methods = {
        "Strength of Schedule": lambda: standings.sos_ranked(games),
        "Win Percentage": lambda: standings.win_pct_ranked(),
        "Points Per Game": lambda: standings.points_per_ranked(),
        "Max Points": lambda: standings.max_points_ranked(),
        "Pythagorean Expectation": lambda: standings.pe_ranked(),
        "GF Per Game": lambda: standings.gf_per_ranked(),
        "GA Per Game": lambda: standings.ga_per_ranked(),
        "GD Per Game": lambda: standings.gd_per_ranked(),
    }

    rank_method = rank_methods.get(selected)
    
    if rank_method:
        ranked_data = rank_method()
        
        df = pd.DataFrame(
            [{"#": rank + 1, "Team": team, selected: round(value, 3)} 
             for rank, (team, value) in enumerate(ranked_data)]
        ).set_index("#")
        
        st.dataframe(df)
     
    st.header("Debug: Win Percentage")
    for team in teams.values():
        st.write(f"{team.name}: {team.get_win_pct()}")

    st.write("Debug: win_pct_ranked")
    st.write(standings.win_pct_ranked())


        
    
if __name__ == "__main__":
    main()
