"""
This script will contain all functions that will be frequently used.
"""
import databaseQueries

def getPlayerAttributeMapping(results, attribute):
    filteredResults = {}
    for result in results:
        playerId = result["pid"]
        playerName = result["name"]
        key = str(playerId) + " -- " + playerName
        filteredResults[key] = result[attribute]
    return filteredResults

"""
Given a playerId, attribute mapping, this function returns 
"""
def getMaximumAndMinimumElements(filteredResults):
    data = filteredResults.values()
    maxValue = max(data)
    minValue = min(data)
    maxElements = []
    minElements = []
    for key in filteredResults.keys():
        if(filteredResults[key]==maxValue):
            maxElements.append(key.split("--")[1].strip())
        elif(filteredResults[key]==minValue):
            minElements.append(key.split("--")[1].strip())
    return (maxElements,minElements)

"""
Given a list of data, it gets binned up.
"""
def binUpData(data):
    bins = range(0,101)
    binValues = [0] * 101
    for value in data:
        binValues[value] += 1
    return (bins,binValues)

"""
Basic function that calls the required database query and prints the result
"""
def getFilteredTeam(cursor, filterParametersList):
    team = databaseQueries.getTeam(cursor, filterParametersList)
    for player in team:
        print str(player["Player_Rating"]) + " - " + player["Name"]

"""
Basic function that calls the database query for player filters and prints the result
"""
def getFilteredPlayers(cursor, filterParameters, ignoredPlayers = [], isGoalKeeper = False):
    result = None
    if(not(isGoalKeeper)):
        result = databaseQueries.getTopOutfieldPlayers(cursor, filterParameters, "Player_Rating", 10, True, ignoredPlayers)
    else:
        result = databaseQueries.getTopGoalKeepers(cursor, filterParameters, "Player_Rating", 10, True, ignoredPlayers)
    for player in result:
        print str(player["pid"]) + " " + player["Name"] + " " + str(player["Player_Rating"]) 

"""
This is an interactive way of constructing filterParameters for a player.
If given a default position, that key,value pair is automatically added.

Select a formation : 2
4-2-3-1 Wide :  GK  LB  CB  CB  RB  CDM  CDM  LM  CAM  RM  ST  


Create filters for : GK
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : LB
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : CB
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : CB
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : RB
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : CDM
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : CDM
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : LM
Hit 'Stop' to stop.
What's the attribute ? PlayerInfo.Position
What's the operation ? IN
What's the value ? ('LW','LM')
What's the attribute ? stop

Create filters for : CAM
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : RM
Hit 'Stop' to stop.
What's the attribute ? stop

Create filters for : ST
Hit 'Stop' to stop.
What's the attribute ? stop
90 - Manuel Neuer
82 - David Alaba
87 - Sergio Ramos
87 - Thiago Silva
83 - Dani Alves
87 - Philipp Lahm
85 - Sergio Busquets
92 - Cristiano Ronaldo
86 - James Rodriguez
90 - Arjen Robben
90 - Zlatan Ibrahimovic

"""
def constructFilter(defaultPosition = None):
    filterParameters = {}
    print "Hit 'Stop' to stop."
    if(defaultPosition!=None):
        filterParameters["PlayerInfo.Position ="] = "'" + defaultPosition + "'"
    while(True):
        key = str(raw_input("What's the attribute ? "))
        if(key.lower().strip() == "stop"):
            break
        if("PlayerInfo.Position" in key):
            filterParameters.pop("PlayerInfo.Position =")
        operation = str(raw_input("What's the operation ? "))
        value = str(raw_input("What's the value ? "))
        key = key + " " + operation
        filterParameters[key] = value
    return filterParameters
