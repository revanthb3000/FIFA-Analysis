"""
This will be the main function where everything starts off.
"""
import databaseQueries
import plottingFunctions
import exampleFilters

def getTeam(filterParameters):
    return

def main():
#     plottingFunctions.plotCurves(15)
#     plottingFunctions.plotCurves(14)
#     plottingFunctions.plotCurves(13)
#     plottingFunctions.plotCurves(12)
    
    connection = databaseQueries.getDatabaseConnection("15.db")
    cursor = databaseQueries.getConnectionCursor(connection)
    
#     exampleFilters.playerFilterExamples(cursor)
    exampleFilters.teamFilterExamples(cursor)
    
    databaseQueries.closeDatabaseConnection(connection)
    return

if __name__ == '__main__':
    main()