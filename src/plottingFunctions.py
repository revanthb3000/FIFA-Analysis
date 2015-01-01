"""
In this script, I'll write all the plotting function that I plan on using. Pyplot will be used.
"""
import numpy as np
import matplotlib.pyplot as plt
import utilityFunctions
import databaseQueries

"""
For a given FIFA version, this function will create plots for each of the stats for both outfield players and goalkeepers.
"""
def plotCurves(fifaVersion):
    finalBaseAttribute = "HEA"
    if(fifaVersion == 15):
        finalBaseAttribute = "PHY"
        
    playerStatsFields = ["PAC","SHO","PAS","DRI",
                        "DEF",finalBaseAttribute,"Ball_Control", 
                        "Crossing", "Curve", "Dribbling", "Finishing", 
                        "Free_Kick_Accuracy","Heading_Accuracy", "Long_Passing", 
                        "Long_Shots", "Marking", "Penalties", "Short_Passing",
                        "Shot_Power", "Sliding_Tackle", "Standing_Tackle", "Volleys", 
                        "Acceleration", "Agility", "Balance","Jumping", "Reactions", 
                        "Sprint_Speed", "Stamina","Strength", "Aggression", "Positioning", 
                        "Interceptions","Vision", "Player_Rating"]
    
    goalkeeperStatsFields = ["GK_DIV", "HAN", "KIC", "REF", "SPE", "POS", "Player_Rating"]

    for attribute in playerStatsFields:
        getOutfieldAttributePlot(attribute, fifaVersion)
        
    for attribute in goalkeeperStatsFields:
        getGoalkeeperAttributePlot(attribute, fifaVersion)

"""
Given an outfield player attribute and a fifaVersion, this function obtains a basic plot of the distribution of values.
"""
def getOutfieldAttributePlot(attribute, fifaVersion):
    connection = databaseQueries.getDatabaseConnection(str(fifaVersion)  + ".db")
    cursor = databaseQueries.getConnectionCursor(connection)
    
    results = databaseQueries.getAllPlayerStats(cursor)
    filteredResults = utilityFunctions.getPlayerAttributeMapping(results, attribute)
    
    fileName = "plots/" + str(fifaVersion) + "/outfieldPlayers/" + attribute + ".png"
    plotDistribution(filteredResults, attribute, fifaVersion, fileName)
    
    databaseQueries.closeDatabaseConnection(connection)

"""
Given a goalkepper player attribute and a fifaVersion, this function obtains a basic plot of the distribution of values.
"""
def getGoalkeeperAttributePlot(attribute, fifaVersion):
    connection = databaseQueries.getDatabaseConnection(str(fifaVersion)  + ".db")
    cursor = databaseQueries.getConnectionCursor(connection)
    
    results = databaseQueries.getAllGoalKeeperStats(cursor)
    filteredResults = utilityFunctions.getPlayerAttributeMapping(results, attribute)
    
    fileName = "plots/" + str(fifaVersion) + "/goalKeepers/" + attribute + ".png"
    plotDistribution(filteredResults, attribute, fifaVersion, fileName)
    
    databaseQueries.closeDatabaseConnection(connection)

"""
Given a dictionary of <playerId -- playerName, attributeValue>, this function computes the mean, standard deviation, maximum, minimum and plots the graph.
A normal distribution is expected.
"""
def plotDistribution(filteredResults, attribute, fifaVersion, fileName):
    t = utilityFunctions.getMaximumAndMinimumElements(filteredResults)
    maximumElements = t[0]
    minimumElements = t[1]
    
    data = filteredResults.values()
    data.sort()
    
    mean = np.mean(data)
    std = np.std(data)
    maximum = max(data)
    minimum = min(data)
    
    print "Mean : " + str(mean)
    print "Standard Deviation : " + str(std)
    print "Max : " + str(maximum) + " by " + str(maximumElements)
    print "Min : " + str(minimum) + " by " + str(minimumElements)
    
    plt.figure()
    
    plt.title(attribute + " plot for FIFA " + str(fifaVersion))
    
    plt.xlabel(attribute)
    plt.ylabel("Number of players with given value")

    binnedData = utilityFunctions.binUpData(data)
    plt.plot(binnedData[0],binnedData[1])

    plt.savefig(fileName)
