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

def main():
#     simpleRun()
    getAttributePlot("PAC", 15)
    return

if __name__ == '__main__':
    main()