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
Given a position, this function returns the top 'numberOfPlayers' players of that position.
Example : getTopPlayersByPosition(cursor, "CM", 5, Player_Rating) returns : 

Ruud Gullit 90
Iniesta 89
Roy Keane 88
Patrick Vieira 88
Bastian Schweinsteiger 88
"""
def getTopPlayersByPosition(cursor, position, sortParameter, numberOfPlayers):
    cursor.execute("Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid WHERE "\
                    + "PlayerInfo.position = '" + position + "' ORDER BY PlayerStats." + sortParameter + " DESC LIMIT " + str(numberOfPlayers) + ";")
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

"""
"""
def getTopPlayers(cursor, filterParameters, sortParameter, numberOfPlayers):
    query = "Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid WHERE "
    
    filterQuery = ""
    keys = filterParameters.keys()
    cnt = 0
    while(cnt < len(keys)):
        key = keys[cnt]
        filterQuery += "PlayerInfo." + key + str(filterParameters[key])
        if(cnt != (len(keys) - 1)):
            filterQuery += " AND "
        cnt += 1
    
    query = query + filterQuery + " ORDER BY PlayerStats." + sortParameter + " DESC LIMIT " + str(numberOfPlayers) + ";"
    
    cursor.execute(query)
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows