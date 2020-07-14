# Creative Commons (CC) 2020 Jonathan Steven Capera Quintana
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

'''
This file contains the logic of Football Championship application that
allows to register teams, matches and calculates the Positions Table at the
end of the Championship.
'''

#Classes for logic
from match import *
from team import *


import itertools
        
class Championship:

    #Constructs a Championship with default attributes:  teams(Team[]),
    #team_pairs((Team(),Team())[]) "A list of tuples of Team()", matches(Match[]),
    #pointsWin(int) and pointsDraw(int)
    
    def __init__(self):
        
        self.teams = []
        self.team_pairs = []
        self.matches =[]
        self.pointsWin = 3
        self.pointsDraw = 1

    #Creates a Team and then adds it to the list of teams
        
    def registerTeam(self,name):
        
        self.teams.append(Team(name))
        
    #Create a list of tuples of Team() by the combination of the registered teams
    #for listing the possible matches
        
    def createPairs(self):
        
        self.team_pairs = list(itertools.combinations(self.teams, 2))

    #Sorts the teams according to the rules
    #1)Max points
    #2)Max goalDifference
    #3)Max goalsFor
        
    def orderTeams(self):
        
        self.teams.sort(key = lambda x: (-x.points,-x.goalsDifference,-x.goalsFor))

    #Creates a match given a tuple of teams (team_pair), goals for team1(goals1)
    #and goals for team2(goals2). It updates the attributes of the teams. Then adds
    #the match to the list of matches and calls the function orderTeams()
    #to sort all the teams
        
    def createMatch (self, team_pair, goals1, goals2):
        
        #Updates goalsFor and goalsAgainst
        team_pair[0].goalsFor += goals1
        team_pair[1].goalsFor += goals2
        team_pair[0].goalsAgainst += goals2
        team_pair[1].goalsAgainst += goals1

        #Updates playedMatches and goalsDifference
        for x in team_pair:
            x.playedMatches += 1
            x.goalsDifference = x.goalsFor - x.goalsAgainst

        #Draw
        if goals1 == goals2:
            for x in team_pair:
                x.drawMatches += self.pointsDraw
                x.points += 1
        #Team1 wins
        elif goals1 > goals2:
            team_pair[0].wonMatches += 1
            team_pair[0].points += self.pointsWin
            team_pair[1].lostMatches += 1
        #Team2 wins
        else:
            team_pair[1].wonMatches += 1
            team_pair[1].points += self.pointsWin
            team_pair[0].lostMatches += 1
            
        #Creates match
        match = Match(team_pair[0], team_pair[1], goals1, goals2)
        
        #Add match to the list of matches
        self.matches.append(match)

        #Sort teams with the results 
        self.orderTeams()
