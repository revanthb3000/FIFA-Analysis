"""
This will be the main function where everything starts off.
"""
import sys
import databaseQueries
import plottingFunctions
import exampleFilters
import formations
import utilityFunctions

def getTeam(filterParameters):
    return

def main():
    argument = ""
    if(len(sys.argv)>1):
        argument = sys.argv[1]
    if(argument=='runAnalysis'):
        plottingFunctions.plotCurves(15)
        plottingFunctions.plotCurves(14)
        plottingFunctions.plotCurves(13)
        plottingFunctions.plotCurves(12)
    elif(argument=="createTeam"):
        utilityFunctions.constructFilter()
    else:
        connection = databaseQueries.getDatabaseConnection("15.db")
        cursor = databaseQueries.getConnectionCursor(connection)
        
        exampleFilters.playerFilterExamples(cursor)
        
        print "\nTeam Example : \n"
        exampleFilters.teamFilterExamples(cursor)
        
        databaseQueries.closeDatabaseConnection(connection)

if __name__ == '__main__':
    main()