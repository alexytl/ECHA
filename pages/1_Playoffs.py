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
    st.markdown("*currently not functional ):")

    all_pts = {team.get_name(): team.get_points() for team in teams.values()}
    all_mp = {team.get_name(): team.get_max_points() for team in teams.values()}
    
    data = []
    for team in teams.values():
        status = " "
        name = team.get_name()
        pts = team.get_points()
        gp = team.get_gp()
        gd = team.get_gd()
        mp = team.get_max_points()
        
        fs_above = sum(1 for other in all_mp if pts > all_mp[other]
                       and other != team)
        fs_below = sum(1 for other in all_pts if mp < all_pts[other]
                       and other != team)
        
        if fs_below >= 6:
            status = "e"
        elif fs_above >= 7:
            status = "y"
        elif fs_above >= 3:
            status = "x"
        elif fs_above == 8:
            status = "z"
        
        data.append([status, name, gp, pts, gd])
            
    picture_df = pd.DataFrame(data, 
                              columns=["Status", "Team", "GP", "PTS", "GD"])
    picture_df.sort_values(by=["PTS", "GD"], 
                           ascending=[False, False], inplace=True)
    ranked_data = [{"#": rank + 1, "Status": row[0], "Team": row[1], 
                    "GP": row[2], "PTS": row[3], "GD": row[4]} for rank, 
                   row in enumerate(picture_df.values)]
    final_df = pd.DataFrame(ranked_data).set_index("#")
    
    
    st.dataframe(final_df)
    st.markdown("Legend:")
    st.markdown("z = Clinched Conference/Nationals Auto-Bid")
    st.markdown("y = Clinched Quarterfinal Bye")
    st.markdown("x = Clinched Playoff Birth")
    st.markdown("e = Eliminated From Playoff Contention")
    
if __name__ == "__main__":
    main()
