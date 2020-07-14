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

class Match:
    
    #Constructs a Match with specified attributes: team1(Team), team2(Team),
    #goals1(int) "Goals For Team1"  and goals2(int) "Goals For Team2"
    
    def __init__(self, team1, team2, goals1, goals2):
        
        self.team1 = team1
        self.team2 = team2
        self.goals1 = goals1
        self.goals2 = goals2
