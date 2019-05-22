# 22/03/2019

'''
Optimization algorithm for routing garbage trucks
'''

import random
import math
import time 
import pandas as pd
import datetime as dt
import random

#---------------------------#
# custom exceptions
class CustomException(Exception):
    '''Base class for all custom exceptions'''
    pass
class OutOfRange(CustomException):
    '''Raised when a number entered is out of a given range'''
    pass

#---------------------------#
# returns the centroid
def getCentroid():
    xSum = 0
    ySum = 0
    for point in binCoordinates:
        xSum += point[0]
        ySum += point[1]

    centroid = (int(xSum / numBins), int(ySum / numBins))
    return centroid

# returns a list of tuples containing x and y coordinates
def genCoordinates(lowerLimit, upperLimit):
    global numBins, coordList
    while(True):
        try:
            numBins = int(input("Enter the number of bins in the locality: "))
            if numBins <= 0 or numBins > 25:
                raise OutOfRange
            else:
                break
        except OutOfRange:
            print("Number of bins entered must be between 1 and 25")
    
    # initializing coordinates list with depot location
    coordList = [(0, 0)]

    for i in range(numBins):
        x = random.randint(lowerLimit, upperLimit)
        y = random.randint(lowerLimit, upperLimit)

        coord = (x, y)

        if coord not in coordList:
            coordList.append(coord)

    return coordList

# reads from csv and converts to pandas dataframe
def genData(csvFile):
    global dataFile

    dataFile = pd.read_csv(csvFile + ".csv")

    data = {}

    for i in range(1, len(coordList)):
        tempList = dataFile.loc[i - 1, :].tolist()
        tempList.pop(0)
        tempCoord = coordList[i]
        data[tempCoord] = tempList

# returns distance matrix - manhattan distance
def getDistance(binCoordinates):
    distMatrix = []
    for i in range(len(binCoordinates)):
        rowList = []
        for j in range(len(binCoordinates)):
            dist = abs(binCoordinates[i][0] - binCoordinates[j][0]) + abs(binCoordinates[i][1] - binCoordinates[j][1])
            rowList.append(dist)
        distMatrix.append(rowList)
    
    return distMatrix


# checks if any dustbin needs to be emptied the following day
def checkBin():
    avg = []
    dayCount = 0
    
    for i in range(len(binCoordinates) - 1):
        avg.append(0)

    dataFile_ = dataFile.drop(columns = ['node'])

    for i in range(len(dataFile_.columns)):
        date = dataFile_.columns[i]
        colList = dataFile_[dataFile_.columns[i]].tolist()
        if i != 0:
            prevColList = dataFile_[dataFile_.columns[i - 1]].tolist()

        nodeList = []   # the bins that are to be emptied next day

        for j in range(len(colList)):   # iterating through levels of each bin
            if i == 0:
                if colList[j] + colList[j] >= 100:
                    nodeList.append(j)
            
            else:
                currAvg = colList[j] - prevColList[j]
                avg[j] = (avg[j] + currAvg)/2
                
                if colList[j] + avg[j] >= 100:
                    nodeList.append(j)
                    avg[j] = 0
        
        if not nodeList:
            print(date, ":\n", "No dustbin to be emptied the following day\n")
        else:
            # display the coordinates to be visited
            if len(nodeList) > 1:
                print(date, ":\n", end = " ")
                for node in nodeList:
                    print(binCoordinates[node + 1], end = " ") 
                print("to be emptied", '\n')
            else:
                for node in nodeList:
                    print(date, ":\n", binCoordinates[node + 1], "to be emptied", '\n')

            router(nodeList, date)
            time.sleep(3)

        
    
        print('-----------------------------------------------------------------\n')


def router(nodeList, date):
    minIndex = 0
    currNodes = [(0, 0)]

    route = []
    nodeDict = {}
    distDict = {}

    for node in nodeList:
        nodeID = node + 1
        currNodes.append(binCoordinates[nodeID])

    # get key from value of dict
    def getKey(val): 
        for key, value in nodeDict.items(): 
            if val == value: 
                return key 
    
        return "Key doesn't exist\n"

    currNodesCopy = currNodes
    if len(currNodes) > 2:
        for node in currNodes:
            nodeDict = {}
            for i in range(len(currNodes)):
                nodeDict[currNodes[i]] = i

            distMat = getDistance(currNodes)

            minDist = 9999
            for i in range(len(currNodesCopy)):
                if i != 0:
                    if distMat[0][i] < minDist:
                        minDist = distMat[0][i]
                        minNode = i
                else:
                    continue

            nodeToRoute = getKey(minNode)

            route.append(nodeToRoute)
            # print(route)
            if len(route) == len(currNodes) - 1:
                break
                break
            currNodes[0] = (999 + nodeToRoute[0], 999 + nodeToRoute[0])
            currNodes.remove(nodeToRoute)
            currNodes.insert(0, nodeToRoute)
    elif len(currNodes) == 2:
        route.append(currNodes[1])

    # return route 
    print("Route :\n(0, 0)", end = " ")

    for node in route:
        print("->", node, end = " ")         

    print('\n')



#---------------------------#
# main
global thresh, centroid, binCoordinates, distance

while(True):
    try:
        locality = int(input("\nEnter the locality ID: "))
        if locality < 0:
            raise OutOfRange
        else:
            break
    except OutOfRange:
        print("Locality IDs must be positive")
    except TypeError:
        print("Must be a positive integer")

# generate random coordinates
binCoordinates = genCoordinates(1, 100)
print("The coordinates are:", binCoordinates)

print("Depot located at:", binCoordinates[0])

# distance matrix
distance = getDistance(binCoordinates)

# generate/import data
csvFile = input("Enter the CSV file to be used: ")
print('\n')
genData(csvFile)

# find the bins that need to be emptied the following day
checkBin()