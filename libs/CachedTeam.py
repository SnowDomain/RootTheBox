
class CachedTeam():
    
    def __init__(self, team_name):
        self.team_name = ""
        self.current_score = 0
        self.scores = []
        
    def add_score(self, score_update):
        self.current_score += int(score_update.value)
        self.scores.append([int(score_update.time_stamp), int(score_update.value)])