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
