from datetime import date

class Game:
    def __init__(self, game_num: int, home: str, away: str, home_score: int, 
                 away_score: int, matchup: int, overtime: bool,
                 game_date: date, time: str, rink: str):
        self._game_num = game_num
        self._home = home
        self._away = away
        self._home_score = home_score
        self._away_score = away_score
        self._matchup = matchup
        self._overtime = overtime
        self._date = game_date
        self._time = time
        self._rink = rink

    @property
    def game_num(self):
        return self._game_num

    @property
    def home(self):
        return self._home
    
    @property
    def away(self):
        return self._away

    @property
    def home_score(self):
        return self._home_score

    @property
    def away_score(self):
        return self._away_score

    @property
    def matchup(self):
        return self._matchup

    @property
    def overtime(self):
        return self._overtime

    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time
    
    @property
    def rink(self):
        return self._rink