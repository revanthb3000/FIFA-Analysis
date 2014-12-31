"""
This will be the main function where everything starts off.
"""
import databaseQueries
import utilityFunctions
import plottingFunctions

"""
Given an outfield player attribute and a fifaVersion, this function obtains a basic plot of the distribution of values.
"""
def getOutfieldAttributePlot(attribute, fifaVersion):
    connection = databaseQueries.getDatabaseConnection(str(fifaVersion)  + ".db")
    cursor = databaseQueries.getConnectionCursor(connection)
    
    results = databaseQueries.getAllPlayerStats(cursor)
    filteredResults = utilityFunctions.getPlayerAttributeMapping(results, attribute)
    
    fileName = "plots/" + str(fifaVersion) + "/outfieldPlayers/" + attribute + ".png"
    plottingFunctions.plotDistribution(filteredResults, attribute, fifaVersion, fileName)
    
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
    plottingFunctions.plotDistribution(filteredResults, attribute, fifaVersion, fileName)
    
    databaseQueries.closeDatabaseConnection(connection)

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

def filterExample(cursor, filterParameters):
    result = databaseQueries.getTopPlayers(cursor, filterParameters, "Player_Rating", 10);
    for player in result:
        print player["Name"] + " " + str(player["Player_Rating"]) 

def main():
    connection = databaseQueries.getDatabaseConnection("15.db")
    cursor = databaseQueries.getConnectionCursor(connection)

    print "\nTest #1 : "
    filterParameters = {"club=" : "'Manchester Utd'", "league=" : "'Barclays PL'", "nation=" : "'England'",
                        "position=" : "'ST'", "Foot=" : "'Right'", "attack_WR=" : "'High'", "defense_WR=" : "'High'",
                        "skills>=" : 3, "weak_foot>=" : 3}
    filterExample(cursor, filterParameters)

    print "\nTest #2 : "
    filterParameters = {"club=" : "'Manchester Utd'", "league=" : "'Barclays PL'",
                        "position=" : "'ST'", "Foot=" : "'Left'",
                        "skills>=" : 3, "weak_foot>=" : 3}
    filterExample(cursor, filterParameters)
    
    print "\nTest #3 : "
    filterParameters = {"club=" : "'Manchester Utd'", "league=" : "'Barclays PL'",
                        "position=" : "'ST'", "Foot=" : "'Right'",
                        "skills>=" : 3, "weak_foot>=" : 3}
    filterExample(cursor, filterParameters)

    print "\nTest #4 : "
    filterParameters = {"league=" : "'Barclays PL'",
                        "position=" : "'ST'", "Foot=" : "'Right'",
                        "skills>=" : 3, "weak_foot>=" : 3}
    filterExample(cursor, filterParameters)
    
    databaseQueries.closeDatabaseConnection(connection)
    return

if __name__ == '__main__':
    main()