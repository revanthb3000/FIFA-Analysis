"""
This function will contain all the queries that I will be using during my analysis.
"""
import sqlite3

def getDatabaseConnection(dbName):
    connection = sqlite3.connect(dbName)
    connection.text_factory = str
    #By using this property, you'll be able to do operations on the result set like row["Ball Control"]
    connection.row_factory = sqlite3.Row
    return connection

def getConnectionCursor(connection):
    return connection.cursor()

def closeDatabaseConnection(connection):
    connection.commit()
    connection.close()
    
"""
This gets all information about all players.
"""
def getAllPlayerStats(cursor, ignoreSpecialCards = True, ignoreLegends = True):
    if(ignoreSpecialCards):
        query = "Select * from (Select MIN(pid) as minPid, * from PlayerInfo GROUP BY Full_Name) PlayerInfo JOIN PlayerStats ON PlayerInfo.minPid = PlayerStats.pid "
    else:
        query = "Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid "
    
    filterQuery = ";"
    if(ignoreLegends):
        filterQuery = " WHERE PlayerInfo.League <> 'Legends';"
        
    query += filterQuery
        
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
This gets all information about all goalkeepers.
"""
def getAllGoalKeeperStats(cursor, ignoreSpecialCards = True, ignoreLegends = True):
    if(ignoreSpecialCards):
        query = "Select * from (Select MIN(pid) as minPid, * from PlayerInfo GROUP BY Full_Name) PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.pid = GoalkeeperStats.pid "
    else:
        query = "Select * from PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.pid = GoalkeeperStats.pid "
    
    filterQuery = ";"
    if(ignoreLegends):
        filterQuery = " WHERE PlayerInfo.League <> 'Legends';"
        
    query += filterQuery
    
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
Given a dictionary of the form {"Parameter>" : value}, this function returns the desired results.

Example : 
filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                    "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                    "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
Basically, we're looking for right footed strikers with 3 star or greater weak foot and skills and who play in the BPL.
So, for the call databaseQueries.getTopOutfieldPlayers(cursor, filterParameters, "Player_Rating", 10, False, []), the results are :

------------------------------
Player            |    Rating
------------------------------
Falcao            |    88
Sergio Aguero     |    87
Sergio Aguero     |    86
Diego Costa       |    86
Wayne Rooney      |    86
Diego Costa       |    85
Edin Dzeko        |    84
Edin Dzeko        |    83
Mario Balotelli   |    82
Samuel Eto'o      |    81
------------------------------

Dzeko and Aguero appear twice because of their In-Forms.

However, if you set ignoreSpecialCards to True, you get : 
------------------------------
Player            |    Rating
------------------------------
Falcao            |    88
Sergio Aguero     |    86
Wayne Rooney      |    86
Diego Costa       |    85
Edin Dzeko        |    83
Mario Balotelli   |    82
Didier Drogba     |    81
Soldado           |    81
Samuel Eto'o      |    81
Stevan Jovetic    |    81
------------------------------

"""
def getTopOutfieldPlayers(cursor, filterParameters, sortParameter, numberOfPlayers, ignoreSpecialCards = True, ignoredPidList = [], ignoreLegends = True):
    query = ""
    if(ignoreSpecialCards):
        query = "Select * from (Select MIN(pid) as minPid, * from PlayerInfo GROUP BY Full_Name) PlayerInfo JOIN PlayerStats ON PlayerInfo.minPid = PlayerStats.pid WHERE "
    else:
        query = "Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid WHERE "
    
    filterQuery = "PlayerInfo.pid NOT IN (" + str(ignoredPidList) + ")"
    filterQuery = filterQuery.replace("([","(").replace("])",")")
    if(ignoreLegends):
        filterQuery += " AND PlayerInfo.League <> 'Legends'"
        
    keys = filterParameters.keys()
    cnt = 0
    while(cnt < len(keys)):
        key = keys[cnt]
        filterQuery += " AND " + key + str(filterParameters[key])
        cnt += 1
    
    query = query + filterQuery + " ORDER BY PlayerStats." + sortParameter + " DESC LIMIT " + str(numberOfPlayers) + ";"
    
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
Same as the above query, but for goalkeepers.
"""
def getTopGoalKeepers(cursor, filterParameters, sortParameter, numberOfPlayers, ignoreSpecialCards = True, ignoredPidList = [], ignoreLegends = True):
    query = ""
    if(ignoreSpecialCards):
        query = "Select * from (Select MIN(pid) as minPid, * from PlayerInfo GROUP BY Full_Name) PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.minPid = GoalkeeperStats.pid WHERE "
    else:
        query = "Select * from PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.pid = GoalkeeperStats.pid WHERE "
    
    filterQuery = "PlayerInfo.pid NOT IN (" + str(ignoredPidList) + ")"
    filterQuery = filterQuery.replace("([","(").replace("])",")")
    if(ignoreLegends):
        filterQuery += " AND PlayerInfo.League <> 'Legends'"
    keys = filterParameters.keys()
    cnt = 0
    while(cnt < len(keys)):
        key = keys[cnt]
        filterQuery += " AND " + key + str(filterParameters[key])
        cnt += 1
    
    query = query + filterQuery + " ORDER BY GoalkeeperStats." + sortParameter + " DESC LIMIT " + str(numberOfPlayers) + ";"
    
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
Given a filterParameters List, this function will construct the best team !
"""
def getTeam(cursor, filterParametersList, sortParameter = "Player_Rating", ignoreSpecialCards = True):
    ignoredPlayersList = []
    team = []
    for filterParameters in filterParametersList:
        player = None
        if("'GK'" in filterParameters.values()):
            player = getTopGoalKeepers(cursor, filterParameters, sortParameter, 1, ignoreSpecialCards, ignoredPlayersList)
        else:
            player = getTopOutfieldPlayers(cursor, filterParameters, sortParameter, 1, ignoreSpecialCards, ignoredPlayersList)
        if(player == []):
            print "No player found for : "
            print filterParameters
            continue
        playerId = player[0]["pid"]
        ignoredPlayersList.append(playerId) #Player can't appear in a team twice.
        team.append(player[0])
    return team
    