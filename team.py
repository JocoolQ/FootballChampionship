class Team:

    #constructs a Team with an specified name(str) and default attributes:
    #playedMatches(int), wonMatches(int), drawMatches(int), lostMatches (int),
    #goalsFor(int) "Goals Scored" , goalsAgainst (int), goalsDifference (int)
    #"GF-GA" and points(int) "Points Scored"
    
    def __init__(self, name):
        
        self.name = name
        self.playedMatches = 0
        self.wonMatches = 0
        self.drawMatches = 0
        self.lostMatches = 0
        self.goalsFor = 0
        self.goalsAgainst = 0
        self.goalsDifference = 0
        self.points = 0
