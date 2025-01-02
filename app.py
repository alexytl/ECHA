import streamlit as st
import pandas as pd
from standings_2 import Standings2
from game_reader_2 import GameReader2

path = ".devcontainer/tank.csv"

def main():
    st.title("ECHA Stats App")
    """
    file = st.file_uploader("Upload CSV File", type="csv")
    
    if file:
        with open("echa.csv", "wb") as f:
            f.write(file.getbuffer())
        csv_path = "echa.csv"
        st.success("Using Uploaded CSV File")
    else:
        csv_path = "tank.csv"
        st.info("Using Default CSV")
    """
    game_reader = GameReader2()
    game_reader.read_csv(path)
        
    games = game_reader.get_games()
    teams = game_reader.get_teams()
    standings = Standings2(teams)
        
    st.header("ECHA Standings")
    standings_data = standings.standings()
    ranked_data = [{"#": rank + 1, **team_data} for rank, 
                       team_data in enumerate(standings_data)]
    standings_df = pd.DataFrame(ranked_data).set_index("#")
    st.dataframe(standings_df)
        
if __name__ == "__main__":
    main()
