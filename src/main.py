"""
This will be the main function where everything starts off.
"""
import sys
import databaseQueries
import plottingFunctions
import exampleFilters
from formations import teamFormations
import utilityFunctions

def getTeam(filterParameters):
    return

def main():
    connection = databaseQueries.getDatabaseConnection("15.db")
    cursor = databaseQueries.getConnectionCursor(connection)
    
    argument = ""
    if(len(sys.argv)>1):
        argument = sys.argv[1]
    if(argument=='runAnalysis'):
        plottingFunctions.plotCurves(15)
        plottingFunctions.plotCurves(14)
        plottingFunctions.plotCurves(13)
        plottingFunctions.plotCurves(12)
    elif(argument=="createTeam"):
        options = teamFormations.keys()
        menu = "Select a formation : \n"
        cnt = 1
        for option in options:
            menu += str(cnt) + ". " + option + "\n"
            cnt += 1
        menu += "\nSelect a formation : "
        selectedOption = int(raw_input(menu))
        selectedFormation = options[selectedOption - 1]
        positions = teamFormations[selectedFormation]
        print selectedFormation + " : ",
        for position in positions:
            print position + " ", 
        
        print "\n"
        filterParametersList = []
        for position in positions:
            print "\nCreate filters for : " + position
            filterParametersList.append(utilityFunctions.constructFilter(position))

        utilityFunctions.getFilteredTeam(cursor, filterParametersList)
    else:        
        exampleFilters.playerFilterExamples(cursor)
        
        print "\nTeam Example : \n"
        exampleFilters.teamFilterExamples(cursor)
        
    databaseQueries.closeDatabaseConnection(connection)

if __name__ == '__main__':
    main()