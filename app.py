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
This file contains the web view of Football Championship application
implemented with the Flask Framework. It uses five templates:
"index.html", "form.html", "registerTeams.html", "registerMatches.html" and
"positionsTable.html"
'''

#Import of Flask Library
from flask import Flask, render_template, redirect, \
    url_for, request, flash, escape

#Import of the application logic
from championship import *

import os
import time

app = Flask(__name__)

app.secret_key = os.urandom(24)

#Instances new Championship (champ) and defines max and min number of teams
champ = Championship()
max_teams = 8
min_teams = 2

#Defines the route and actions for the "index.html" template

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            #Resets Championship
            champ.teams= []
            champ.matches = []
            champ.team_pairs = []
            
            # Number of teams
            n = int(escape(request.form["teams"]))

            #Evaluates the min and max teams allowed and launches
            #an error if the values are not correct
            if n > max_teams:
                flash("Error:"+ str(max_teams) +" is the maximum number of possible teams.")
            elif n < min_teams:
                flash("Error: Number must be greater than one.")
            else:
                #Renders the "registerTeams.html" template with the
                #argument n
                return render_template(
                    "registerTeams.html",
                    n=n)
            
        #Captures any exception and displays error
        except Exception as e:
            print(e)
            flash("Error: Please insert valid data."+str(e))
    # else:
    
    #Renders the "form.html" template 
    return render_template("form.html")

#Defines the route and actions for the "registerMatches.html" template

@app.route("/registerMatches/", methods=["GET", "POST"])
def registerMatches():
    
    if request.method == "POST":
        try:
            teams = []
            i=1
            
            #Create an array of team names
            for regs in request.form:
                teams.append(str(escape(request.form["team"+str(i)])))
                i += 1
            #verify unique id
                
            #Registers each team with its name   
            for t in teams:
                champ.registerTeam(t)

            #Creates a list of possible matches (champ.team_pairs)
            champ.createPairs()
            
            matches = []

            #Creates a list of tuples with the names of team pairs
            #for the matches
            for pair in champ.team_pairs:
                p = (pair[0].name,pair[1].name)
                matches.append(p)

            #Renders the "registerMatches.html" template with the
            #argument matches
            return render_template(
                "registerMatches.html",
                matches=matches)
        
        #Captures any exception and displays error
        except Exception as e:
            print(e)
            flash("Error: Please insert valid data: "+str(e))
    return render_template("registerTeams.html")

#Defines the route and actions for the "positionsTable.html" template

@app.route("/positionsTable/", methods=["GET", "POST"])
def positionsTable():
    
    if request.method == "POST":
        try:
            #Creates the matches for the Championship with the fields
            #of the form obtained from "registerMatches.html"
            for i in range(len(champ.team_pairs)):
                champ.createMatch(champ.team_pairs[i],
                                   int(escape(request.form["goalsT1M"+str(i)])),
                                       int(escape(request.form["goalsT2M"+str(i)])))
            #verify goals greater than zero

            #Sends head and data for the Positions Table                            
            data = [] #a list of the atributes for each team                        
            for team in champ.teams:
                head = vars(team) #Description of each atribute of Team
                d = []
                for item in head:
                    d.append(head[item]) #Adds each atrribute of the actual team
                data.append(d) #Adds a new register to the list

            #Renders the "positionsTable.html" template with the arguments
            #head and data
            return render_template(
                "positionsTable.html",
                head = head,
                data = data)
        
        #Captures any exception and displays error
        except Exception as e:
            print(e)
            flash("Error: Please insert valid data: "+str(e))
    #else:

    #Renders the "form.html" template in other case
    return render_template("form.html")

if __name__ == "__main__":
    app.run()
