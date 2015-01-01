"""
This is a file where I just put in examples and play around with the functions.
A test bed of sorts.
"""

import databaseQueries

def getFilteredPlayers(cursor, filterParameters, ignoredPlayers = []):
    result = databaseQueries.getTopPlayers(cursor, filterParameters, "Player_Rating", 10, True, ignoredPlayers)
    for player in result:
        print str(player["pid"]) + " " + player["Name"] + " " + str(player["Player_Rating"]) 

def filterExamples(cursor):
    print "\nTest #1 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'", "PlayerInfo.nation=" : "'England'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'", "PlayerInfo.attack_WR=" : "'High'", "PlayerInfo.defense_WR=" : "'High'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    getFilteredPlayers(cursor, filterParameters)

    print "\nTest #2 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Left'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    getFilteredPlayers(cursor, filterParameters)
    
    print "\nTest #3 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    getFilteredPlayers(cursor, filterParameters)

    ignorePlayers = [45] #Sergio Aguero is ignored.
    print "\nTest #4 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    getFilteredPlayers(cursor, filterParameters, ignorePlayers)
    
    print "\nTest #5 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3, "PlayerStats.PAC>=" : 80}
    getFilteredPlayers(cursor, filterParameters)