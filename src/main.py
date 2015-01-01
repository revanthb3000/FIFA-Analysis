"""
This will be the main function where everything starts off.
"""
import databaseQueries
import plottingFunctions

def filterExample(cursor, filterParameters):
    ignorePlayers = [45] #Sergio Aguero is ignored.
    result = databaseQueries.getTopPlayers(cursor, filterParameters, "Player_Rating", 10, True, ignorePlayers)
    for player in result:
        print str(player["pid"]) + " " + player["Name"] + " " + str(player["Player_Rating"]) 

def main():
    plottingFunctions.plotCurves(15)
    plottingFunctions.plotCurves(14)
    plottingFunctions.plotCurves(13)
    plottingFunctions.plotCurves(12)
    
    connection = databaseQueries.getDatabaseConnection("15.db")
    cursor = databaseQueries.getConnectionCursor(connection)

    print "\nTest #1 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'", "PlayerInfo.nation=" : "'England'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'", "PlayerInfo.attack_WR=" : "'High'", "PlayerInfo.defense_WR=" : "'High'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    filterExample(cursor, filterParameters)

    print "\nTest #2 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Left'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    filterExample(cursor, filterParameters)
    
    print "\nTest #3 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    filterExample(cursor, filterParameters)

    print "\nTest #4 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    filterExample(cursor, filterParameters)
    
    print "\nTest #5 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3, "PlayerStats.PAC>=" : 80}
    filterExample(cursor, filterParameters)
    
    databaseQueries.closeDatabaseConnection(connection)
    return

if __name__ == '__main__':
    main()