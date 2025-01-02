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
        home_records_df = pd.DataFrame(standings.home_records(games))
        st.dataframe(home_records_df)