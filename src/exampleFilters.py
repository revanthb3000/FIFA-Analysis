"""
This is a file where I just put in examples and play around with the functions.
A test bed of sorts.
"""
import utilityFunctions

"""
Just a couple of examples on how to generate a team for constraints.

For the first example the result is : 
86 - Thibaut Courtois
87 - Sergio Ramos
86 - Vincent Kompany
82 - Filipe Luis
83 - Dani Alves
86 - Yaya Toure
89 - Iniesta
85 - Toni Kroos
93 - Lionel Messi
92 - Cristiano Ronaldo
88 - Robin van Persie

in a 4-4-2 diamond. Seems pretty good :D
"""
def teamFilterExamples(cursor):
    #For this example, I'll go for a 4-4-2 Diamond which will have 1 GK, 2 CBs, LB, RB, CDM, 2CMs, CAM, 2STs
    #Overall Constraints are that I want a team that consists only of BPL or La Liga Players.
    baseConstraints = {"PlayerInfo.league IN":"('Barclays PL','Liga BBVA')"}
    
    filterParametersList = []
    
    #GK First. Let's have a goal keeper with 85+ Reflexes
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position="] = "'GK'"
    newConstraint["GoalkeeperStats.REF>="] = 85
    filterParametersList.append(newConstraint)
    
    #CBs now. Good pacy defenders needed.
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position="] = "'CB'"
    newConstraint["PlayerStats.PAC>="] = 70
    filterParametersList.append(newConstraint)
    filterParametersList.append(newConstraint)
    
    #Full backs. Want good crossers here.
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position="] = "'LB'"
    newConstraint["PlayerStats.Crossing>="] = 70
    filterParametersList.append(newConstraint)
    
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position="] = "'RB'"
    newConstraint["PlayerStats.Crossing>="] = 70
    filterParametersList.append(newConstraint)
    
    #CDM now - want someome with 85+ DEF and 85+ PAS
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('CDM','CM')"
    newConstraint["PlayerStats.DEF>="] = 80
    newConstraint["PlayerStats.PAS>="] = 80
    filterParametersList.append(newConstraint)
    
    #CM now - want someone with 86+ PAS and 75+ PAC
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('CM')"
    newConstraint["PlayerStats.PAC>="] = 75
    newConstraint["PlayerStats.PAS>="] = 86
    filterParametersList.append(newConstraint)
    
    #My next CM must have 85+ PAS and 80+ Long_Shots
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('CM')"
    newConstraint["PlayerStats.Long_Shots>="] = 80
    newConstraint["PlayerStats.PAS>="] = 86
    filterParametersList.append(newConstraint)
    
    #CAM - I want someone with 85+ DRI and 90+ Vision
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('CAM','CF')"
    newConstraint["PlayerStats.DRI>="] = 85
    newConstraint["PlayerStats.Vision>="] = 90
    filterParametersList.append(newConstraint)
    
    #First ST - I want someone with 90+ shooting and a right footed player with 4 star skills
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('ST','CF','LW','LM')"
    newConstraint["PlayerInfo.skills>="] = 4
    newConstraint["PlayerInfo.Foot="] = "'Right'"
    newConstraint["PlayerStats.SHO>="] = 90
    filterParametersList.append(newConstraint)
    
    #Ditto but a left footed player here.
    newConstraint = baseConstraints.copy()
    newConstraint["PlayerInfo.position IN"] = "('ST','CF','RW','RM')"
    newConstraint["PlayerInfo.skills>="] = 4
    newConstraint["PlayerInfo.Foot="] = "'Left'"
    newConstraint["PlayerStats.SHO>="] = 90
    filterParametersList.append(newConstraint)
    
    print "4-4-2 Diamond : "
    utilityFunctions.getFilteredTeam(cursor, filterParametersList)

"""
Several examples on how to use filters to find top players for a criteria.
"""
def playerFilterExamples(cursor):
    print "\nTest #1 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'", "PlayerInfo.nation=" : "'England'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'", "PlayerInfo.attack_WR=" : "'High'", "PlayerInfo.defense_WR=" : "'High'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters)

    print "\nTest #2 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Left'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters)
    
    print "\nTest #3 : "
    filterParameters = {"PlayerInfo.club=" : "'Manchester Utd'", "PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters)

    ignorePlayers = [45] #Sergio Aguero is ignored.
    print "\nTest #4 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position IN " : "('ST','CF','LM')", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters, ignorePlayers)
    
    print "\nTest #5 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'ST'", "PlayerInfo.Foot=" : "'Right'",
                        "PlayerInfo.skills>=" : 3, "PlayerInfo.weak_foot>=" : 3, "PlayerStats.PAC>=" : 80}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters)
    
    print "\nTest #6 : "
    filterParameters = {"PlayerInfo.league=" : "'Barclays PL'",
                        "PlayerInfo.position=" : "'GK'", "PlayerInfo.Foot=" : "'Right'",
                        "GoalkeeperStats.REF>=" : 85}
    utilityFunctions.getFilteredPlayers(cursor, filterParameters, isGoalKeeper = True)
    