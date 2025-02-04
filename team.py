class Team:
    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ot_ws = 0
        self.ot_ls = 0
        self.goals_f = 0
        self.goals_a = 0
        self.points = 0
        self.games_p = 0
        
    #stat-adjusting methods
    def add_win(self):
        self.wins += 1
        self.points += 3
        self.games_p += 1
        
    def add_loss(self):
        self.losses += 1
        self.games_p += 1
      
    def add_ot_w(self):
        self.ot_ws += 1
        self.points += 2
        self.games_p += 1
      
    def add_ot_l(self):
        self.ot_ls += 1
        self.points += 1
        self.games_p += 1
        
    def add_gf(self, x: int):
        self.goals_f += x
        
    def add_ga(self, x: int):
        self.goals_a += x
        
    #home/away getters
    def get_home_record(self, games):
        w = 0
        l = 0
        otw = 0
        otl = 0
        
        for game in games:
            if game.home == self.name:
                if game.time != "Final":
                    continue
                elif game.home_score > game.away_score:
                    if game.overtime:
                        otw += 1
                    else:
                        w += 1
                else:
                    if game.overtime:
                        otl += 1
                    else:
                        l += 1
        return f"{w}-{otw}-{otl}-{l}"
    
    def get_away_record(self, games):
        w = 0
        l = 0
        otw = 0
        otl = 0
            
        for game in games:
            if game.away == self.name:
                if game.time != "Final":
                    continue
                elif game.away_score > game.home_score:
                    if game.overtime:
                        otw += 1
                    else:
                        w += 1
                else:
                    if game.overtime:
                        otl += 1
                    else:
                        l += 1
        return f"{w}-{otw}-{otl}-{l}"
                            
    def get_home_win_pct(self, games):
        w = 0
        l = 0
        for game in games:
            if game.home != self.name:
                continue
            elif game.time != "Final":
                continue
            elif game.home_score > game.away_score:
                w += 1
            else:
                l += 1
        return float(w/(w+l))
                
    def get_away_win_pct(self, games):
        w = 0
        l = 0
        for game in games:
            if game.away != self.name:
                continue
            elif game.time != "Final":
                continue
            elif game.away_score > game.home_score:
                w += 1
            else:
                l += 1
        return float(w/(w+l))
                
    #goal getters
    def get_gd(self):
        return self.goals_f - self.goals_a
    
    def get_gf_per(self):
        return float(self.goals_f / self.games_p) if self.games_p >= 0 else 0
    
    def get_ga_per(self):
        return float(self.goals_a / self.games_p) if self.games_p >= 0 else 0
    
    def get_gd_per(self):
        return float(self.get_gd() / self.games_p) if self.games_p >= 0 else 0
     
    #advanced-record getters
    def get_win_pct(self):
        return float((self.wins + self.ot_ws) / self.games_p) if self.games_p >= 0 else 0
    
    def get_points_per(self):
        return float(self.points / self.games_p) if self.games_p >= 0 else 0
    
    def get_pe(self):
        if self.goals_f + self.goals_a == 0:
            return 0
        
        gf_pythd = float(self.goals_f ** 2.05)
        ga_pythd = float(self.goals_a ** 2.05)
        return gf_pythd / (gf_pythd + ga_pythd)
    
    def get_max_points(self):
        return self.points + 3 * (16 - self.games_p)
    
    #basic getters
    def get_name(self):
        return self.name
    
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.losses
    
    def get_ot_ws(self):
        return self.ot_ws
    
    def get_ot_ls(self):
        return self.ot_ls
    
    def get_gf(self):
        return self.goals_f
    
    def get_ga(self):
        return self.goals_a
    
    def get_points(self):
        return self.points
    
    def get_gp(self):
        return self.games_p
