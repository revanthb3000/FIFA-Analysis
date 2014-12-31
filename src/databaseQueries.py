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
def getAllPlayerStats(cursor):
    cursor.execute("Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid;")
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
This gets all information about all goalkeepers.
"""
def getAllGoalKeeperStats(cursor):
    cursor.execute("Select * from PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.pid = GoalkeeperStats.pid;")
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
So, for the call databaseQueries.getTopPlayers(cursor, filterParameters, "Player_Rating", 10, False), the results are :

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
def getTopPlayers(cursor, filterParameters, sortParameter, numberOfPlayers, ignoreSpecialCards = True):
    query = ""
    if(ignoreSpecialCards):
        query = "Select * from (Select MIN(pid) as minPid, * from PlayerInfo GROUP BY Full_Name) PlayerInfo JOIN PlayerStats ON PlayerInfo.minPid = PlayerStats.pid WHERE "
    else:
        query = "Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid WHERE "
    
    filterQuery = ""
    keys = filterParameters.keys()
    cnt = 0
    while(cnt < len(keys)):
        key = keys[cnt]
        filterQuery += key + str(filterParameters[key])
        if(cnt != (len(keys) - 1)):
            filterQuery += " AND "
        cnt += 1
    
    query = query + filterQuery + " ORDER BY PlayerStats." + sortParameter + " DESC LIMIT " + str(numberOfPlayers) + ";"
    
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows