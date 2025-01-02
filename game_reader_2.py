import csv 
from datetime import datetime
from game import Game
from team import Team

class GameReader2:
    def __init__(self):
        self.games = []
        self.teams = {}
        
    def read_csv(self, file_path: str):
        with open(file_path, newline = '', encoding = 'utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for row in reader:
                game_num = int(row[0].strip())
                g_date = datetime.strptime(row[1].strip(), "%m/%d/%Y").date()
                home = row[2].strip()
                home_score = int(row[3].strip()) if row[3].strip() else 0
                away = row[4].strip()
                away_score = int(row[5].strip()) if row[5].strip() else 0
                rink = row[6].strip()
                time = row[7].strip()
                overtime = (row[8].strip() == "1") if row[8].strip() else False
                matchup = int(row[9].strip())
                
                game = Game(game_num, home, away, home_score, away_score,
                            matchup, overtime, g_date, time, rink)
                
                self.games.append(game)
                
                if home not in self.teams:
                    self.teams[home] = Team(home)
                if away not in self.teams:
                    self.teams[away] = Team(away)
         
                if time != 'Final':
                    continue
                
                self.update_team_stats(self.teams[home], self.teams[away], 
                                       home_score, away_score, overtime)
                    
    def update_team_stats(self, home_: Team, away_: Team, h_score: int,
                          a_score: int, ot: bool):
        home_.add_gf(h_score)
        home_.add_ga(a_score)
        away_.add_gf(a_score)
        away_.add_ga(h_score)
        
        if h_score > a_score:
            if ot:
                home_.add_ot_w()
                away_.add_ot_l()
            else:
                home_.add_win()
                away_.add_loss()
        else:
            if ot:
                away_.add_ot_w()
                home_.add_ot_l()
            else:
                away_.add_win()
                home_.add_loss()
                
    def get_games(self):
        return self.games
    
    def get_teams(self):
        return self.teams