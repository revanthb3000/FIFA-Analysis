"""
In this script, I'll write all the plotting function that I plan on using. Pyplot will be used.
"""
import numpy as np
import matplotlib.pyplot as plt
import utilityFunctions

"""
Given a dictionary of <playerId -- playerName, attributeValue>, this function computes the mean, standard deviation, maximum, minimum and plots the graph.
A normal distribution is expected.
"""
def plotDistribution(filteredResults, attribute, fifaVersion, fileName):
    t = utilityFunctions.getMaximumAndMinimumElements(filteredResults)
    maximumElements = t[0]
    minimumElements = t[1]
    
    data = filteredResults.values()
    data.sort()
    
    mean = np.mean(data)
    std = np.std(data)
    maximum = max(data)
    minimum = min(data)
    
    print "Mean : " + str(mean)
    print "Standard Deviation : " + str(std)
    print "Max : " + str(maximum) + " by " + str(maximumElements)
    print "Min : " + str(minimum) + " by " + str(minimumElements)
    
    plt.figure()
    
    plt.title(attribute + " plot for FIFA " + str(fifaVersion))
    
    plt.xlabel(attribute)
    plt.ylabel("Number of players with given value")

    binnedData = utilityFunctions.binUpData(data)
    plt.plot(binnedData[0],binnedData[1])

    plt.savefig(fileName)