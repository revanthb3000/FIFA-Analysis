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
    
def getAllPlayerStats(cursor):
    cursor.execute("Select * from PlayerInfo JOIN PlayerStats ON PlayerInfo.pid = PlayerStats.pid;")
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows

def getAllGoalKeeperStats(cursor):
    cursor.execute("Select * from PlayerInfo JOIN GoalkeeperStats ON PlayerInfo.pid = GoalkeeperStats.pid;")
    rows = []
    for row in cursor.fetchall():
        rows.append(row)
    return rows