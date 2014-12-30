"""
This will be the main function where everything starts off.
"""
import databaseQueries
import utilityFunctions
import plottingFunctions

"""
A sample run of connecting to the database.
"""
def simpleRun():
    connection = databaseQueries.getDatabaseConnection("15.db")
    cursor = databaseQueries.getConnectionCursor(connection)
    results = databaseQueries.getAllPlayerStats(cursor)
    cnt = 0
    for result in results:
        print result.keys()
        print result
        cnt += 1
        if(cnt > 100):
            break
    databaseQueries.closeDatabaseConnection(connection)

"""
Given an attribute and a fifaVersion, this function obtains a basic plot of the distribution of values.
"""
def getAttributePlot(attribute, fifaVersion):
    connection = databaseQueries.getDatabaseConnection(str(fifaVersion)  + ".db")
    cursor = databaseQueries.getConnectionCursor(connection)
    results = databaseQueries.getAllPlayerStats(cursor)
    filteredResults = utilityFunctions.getPlayerAttributeMapping(results, attribute)
#     print filteredResults
    plottingFunctions.plotDistribution(filteredResults, attribute, fifaVersion)
    databaseQueries.closeDatabaseConnection(connection)

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

    for attribute in playerStatsFields:
        getAttributePlot(attribute, fifaVersion)
        

def main():
#     simpleRun()
    plotCurves(15)
    plotCurves(14)

    return

if __name__ == '__main__':
    main()