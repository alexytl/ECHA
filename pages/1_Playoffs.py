import streamlit as st
import pandas as pd
from team import Team
from game_reader_2 import GameReader2
import os

path = os.path.join(os.getcwd(), '.devcontainer', 'dex.csv')


def main():
    st.title("Playoffs")
    
    game_reader = GameReader2()
    game_reader.read_csv(path)
    teams = game_reader.get_teams()
    
    # Picture section
    st.header("Playoff Picture")

    all_pts = {team.get_name(): team.get_points() for team in teams.values()}
    all_mp = {team.get_name(): team.get_points() for team in teams.values()}
    
    data = []
    for team in teams.values():
        status = " "
        name = team.get_name()
        pts = team.get_points()
        gp = team.get_gp()
        gd = team.get_gd()
        mp = team.get_max_points()
        
        fs_above = sum(pts > all_mp[other] 
                       for other in all_pts if other != name)
        fs_below = sum(mp < all_pts[other] 
                       for other in all_mp if other != name)
        
        if fs_below >= 6:
            status = "e"
        elif fs_above == 8:
            status = "z"
        elif fs_above >= 7:
            status = "y"
        elif fs_above >= 3:
            status = "x"
        
        data.append([status, team, gp, pts, gd])
            
    picture_df = pd.DataFrame(data, 
                              columns=["Status", "Team", "GP", "PTS", "GD"])
    
    picture_df.sort_values(by=["PTS", "GD"], 
                           ascending=[False, False], inplace=True)

    st.dataframe(picture_df)
    st.markdown("Legend:")
    st.markdown("z = Clinched Conference/National Bid")
    st.markdown("y = Clinched Quarterfinal Bye")
    st.markdown("x = Clinched Playoff Birth")
    st.markdown("e = Eliminated From Playoff Contention")
    
if __name__ == "__main__":
    main()
