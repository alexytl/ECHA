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
    
    # Debug: Print the teams to check if they are loaded correctly
    st.write(f"Loaded teams: {[team.get_name() for team in teams]}")
    
    # Picture section
    st.header("Playoff Picture")

    all_pts = {team.get_name(): team.get_points() for team in teams}
    all_mp = {team.get_name(): team.get_max_points() for team in teams}
    
    data = []
    for team in teams:
        status = " "
        name = team.get_name()
        pts = team.get_points()
        gp = team.get_gp()
        gd = team.get_gd()
        mp = team.get_max_points()
        
        # Debugging the points and max points of each team
        st.write(f"Processing Team: {name}, PTS: {pts}, MP: {mp}, GP: {gp}, GD: {gd}")
        
        fs_above = sum(pts > all_mp[other] 
                       for other in all_pts if other != name)
        fs_below = sum(mp < all_pts[other] 
                       for other in all_mp if other != name)
        
        # Debugging the calculated values of fs_above and fs_below
        st.write(f"fs_above: {fs_above}, fs_below: {fs_below}")
        
        if fs_below >= 6:
            status = "e"
        elif fs_above == 8:
            status = "z"
        elif fs_above >= 7:
            status = "y"
        elif fs_above >= 3:
            status = "x"
        
        # Debugging the status after calculation
        st.write(f"Status for {name}: {status}")
        
        data.append([status, team, gp, pts, gd])
            
    picture_df = pd.DataFrame(data, 
                              columns=["Status", "Team", "GP", "PTS", "GD"])
    
    picture_df.sort_values(by=["PTS", "GD"], 
                           ascending=[False, False], inplace=True)
    
    # Debugging the generated DataFrame
    st.write("Picture DataFrame:", picture_df)

    st.dataframe(picture_df)
    st.markdown("Legend:")
    st.markdown("z = Clinched Conference/National Bid")
    st.markdown("y = Clinched Quarterfinal Bye")
    st.markdown("x = Clinched Playoff Birth")
    st.markdown("e = Eliminated From Playoff Contention")
    
if __name__ == "__main__":
    main()
