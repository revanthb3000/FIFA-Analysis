"""
This function will contain all functions that will be frequently used.
"""

def getPlayerAttributeMapping(results, attribute):
    filteredResults = {}
    for result in results:
        playerId = result["pid"]
        playerName = result["name"]
        key = str(playerId) + " -- " + playerName
        filteredResults[key] = result[attribute]
    return filteredResults

"""
Given a playerId, attribute mapping, this function returns 
"""
def getMaximumAndMinimumElements(filteredResults):
    data = filteredResults.values()
    maxValue = max(data)
    minValue = min(data)
    maxElements = []
    minElements = []
    for key in filteredResults.keys():
        if(filteredResults[key]==maxValue):
            maxElements.append(key.split("--")[1].strip())
        elif(filteredResults[key]==minValue):
            minElements.append(key.split("--")[1].strip())
    return (maxElements,minElements)