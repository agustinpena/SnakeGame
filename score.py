# this is for the Scoreboard class

IND_SCORE = 1


class Score:

    def __init__(self):
        self.current = 0

    def increase(self):
        self.current += IND_SCORE

    def get(self):
        return self.current
