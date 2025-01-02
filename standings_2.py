class Standings2:
    def __init__(self, teams: dict):
        self.teams = list(teams.values())
        
    def standings(self):
        self.teams.sort(key=self.standings_helper, reverse=True)
        return [{"Team": team.get_name(), "GP": team.get_gp(),
                 "W": team.get_wins(), "L": team.get_losses(),
                 "OTW": team.get_ot_ws(), "OTL": team.get_ot_ls(),
                 "GF": team.get_gf(), "GA": team.get_ga(),
                 "GD": team.get_gd(), "PTS": team.get_points()}
                for team in self.teams]
                        
    def standings_helper(self, team):
        return (team.get_points(), team.get_wins(),
                (team.get_wins() + team.get_ot_ws()))
            
    def home_records(self, games):
        records = []
        for team in self.teams:
            record = team.get_home_record(games)
            win_pct = team.get_home_win_pct(games)
            records.append({"Team": team.name, "Record": record, 
                            "W%": win_pct})
        records.sort(key=lambda x: x["w%"], reverse=True)
        return records
        
    def away_records(self, games):
        records = []
        for team in self.teams:
            record = team.get_away_record(games)
            win_pct = team.get_away_win_pct(games)
            records.append((team.name, record, win_pct))
        records.sort(key = lambda x: x[2], reverse = True)
        print(f"{'Team':<28} {'Away Record':<15} {'Win Pct':<8}")
        print("-" * 54)
        self.print_records(records)
        
    def print_records(self, records):
        for name, record, pct in records:
            print(f"{name:<28} {record:<15} {pct:.3f}")
            
    def away_rinks(self, games):
        rinks = {}
        for game in games:
            if game.rink not in rinks:
                rinks[game.rink] = {"away_wins": 0, "games": 0}
            rinks[game.rink]["games"] += 1
            if game.away_score > game.home_score:
                rinks[game.rink]["away_wins"] += 1
            
        for rink, stats in rinks.items():
            stats["away_win_pct"] = (
                stats["away_wins"] / stats["games"] if stats["games"] > 0 else 0)
                                                        
        sorted_rinks = sorted(rinks.items(),
                              key = lambda x: x[1]["away_win_pct"])
        j = f"{'Rink':<33} {'Away Win Pct':<15} {'Games':<8} "
        j += f"{'Away Wins':<8}"
        print(j)
        print("-" * 70)
        for rink, stats in sorted_rinks:
            l = f"{rink:<33} {stats['away_win_pct']:.3f}           "
            l += f"{stats['games']:<8} {stats['away_wins']:<8}"
            print(l)
            
    def gf_per_ranked(self):
        gf = {}
        for team in self.teams:
            gf[team.name] = team.get_gf_per()
            
        sorted_gf = sorted(gf.items(), key = lambda x: x[1], reverse = True)
        return sorted_gf
            
    def ga_per_ranked(self):
        ga = {}
        for team in self.teams:
            ga[team.name] = team.get_ga_per()
            
        sorted_ga = sorted(ga.items(), key = lambda x: x[1], reverse = False)
        return sorted_ga
            
    def gd_per_ranked(self):
        gd = {}
        for team in self.teams:
            gd[team.name] = team.get_gd_per()
            
        sorted_gd = sorted(gd.items(), key = lambda x: x[1], reverse = True)
        return sorted_gd
        
    def pe_ranked(self):
        pe = {}
        for team in self.teams:
            pe[team.name] = team.get_pe()
            
        sorted_pe = sorted(pe.items(), key = lambda x: x[1], reverse = True)
        return sorted_pe
            
    def win_pct_ranked(self):
        wp = {}
        for team in self.teams:
            wp[team.name] = team.get_win_pct()
            
        sorted_wp = sorted(wp.items(), key = lambda x: x[1], reverse = True)
        return sorted_wp
            
    def points_per_ranked(self):
        ppg = {}
        for team in self.teams:
            ppg[team.name] = team.get_points_per()
            
        sorted_ppg = sorted(ppg.items(), key = lambda x: x[1], reverse = True)
        return sorted_ppg
            
    def max_points_ranked(self):
        mp = {}
        for team in self.teams:
            mp[team.name] = team.get_max_points()
            
        sorted_mp = sorted(mp.items(), key = lambda x: x[1], reverse = True)
        return sorted_mp
    
        
    def sos_ranked(self, games):
        sos = {}
        for team in self.teams:
            opps = []
            for game in games:
                if game.time != "Final":
                    continue
                elif game.home == team.name:
                    opps.append(game.away)
                elif game.away == team.name:
                    opps.append(game.home)
                
            owp = 0
            oowp = 0
            for opponent in opps:
                opp = next(t for t in self.teams if t.name == opponent)
                owp += opp.get_win_pct()
                    
                opp_opps = []
                for game in games:
                    if game.time != "Final":
                        continue
                    elif game.home == opp.name:
                        opp_opps.append(game.away)
                    elif game.away == opp.name:
                            opp_opps.append(game.home)
                    
                oowp_sum = 0
                for opp_ in opp_opps:
                    opp_opp = next(t for t in self.teams if t.name == opp_)
                    oowp_sum += opp_opp.get_win_pct()
                oowp += (oowp_sum / len(opp_opps)) if opp_opps else 0
            
            owp = owp / len(opps) if opps else 0
            oowp = oowp / len(opps) if opps else 0
        
            sos[team.name] = ((3 * owp) + (0 * oowp)) / 3
            
        sorted_sos = sorted(sos.items(), key = lambda x: x[1], reverse = True)
        return sorted_sos
        
