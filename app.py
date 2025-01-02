import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
    st.header("Standings")
    standings_data = standings.standings()
    ranked_data = [{"#": rank + 1, **team_data} for rank, 
                       team_data in enumerate(standings_data)]
    standings_df = pd.DataFrame(ranked_data).set_index("#")
    st.dataframe(standings_df)
        
    #rankings
    st.header("Rankings")
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
    
    #graphing
    st.header("Graphs")
    st.subheader("currently displaying incorrectly!")
    x = st.selectbox("Select x-axis: ", stats)
    y = st.selectbox("Select y-axis: ", stats)
    
    x_data = [value for _, value in rank_methods[x]()]
    y_data = [value for _, value in rank_methods[y]()]
    team_names = [team for team, _ in rank_methods[x]()]
    
    if x_data and y_data:
        fig, ax = plt.subplots()
        ax.scatter(x_data, y_data)
        for i, team in enumerate(team_names):
            ax.text(x_data[i], y_data[i], team, fontsize=8)
    
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")
        st.pyplot(fig)
        
    
if __name__ == "__main__":
    main()
