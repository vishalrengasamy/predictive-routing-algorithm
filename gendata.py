# '''
# Generates data (level of garbage filled over a period of a week) for each bin location
# '''

# import numpy as np
# import pandas as pd
# import datetime as dt
# import random

# # returns a list of tuples containing x and y coordinates
# def genCoordinates(lowerLimit, upperLimit):
#     global numBins, coordList
#     while(True):
#         try:
#             numBins = int(input("Enter the number of bins in the locality: "))
#             if numBins <= 0 or numBins > 25:
#                 raise OutOfRange
#             else:
#                 break
#         except OutOfRange:
#             print("Number of bins entered must be between 1 and 25")
    
#     # initializing coordinates list with depot location
#     coordList = [(0, 0)]

#     for i in range(numBins):
#         x = random.randint(lowerLimit, upperLimit)
#         y = random.randint(lowerLimit, upperLimit)

#         coord = (x, y)

#         if coord not in coordList:
#             coordList.append(coord)

#     return coordList


# def genData():
#     global dataFile

#     dataFile = pd.read_csv("data.csv")

#     data = {}

#     for i in range(1, len(coordList)):
#         tempList = dataFile.loc[i - 1, :].tolist()
#         tempList.pop(0)
#         tempCoord = coordList[i]
#         data[tempCoord] = tempList

#     print("Data: \n")
#     for key in data:
#         print(str(key) + ' -> ' + str(data[key]))


    
# # def checkBin():
# #     avg = []
# #     dayCount = 0
    
# #     for i in range(len(binCoordinates) - 1):
# #         avg.append(0)
# #     # print(len(avg))
# #     dataFile_ = dataFile.drop(columns = ['node'])
# #     # print(dataFile_.head())
# #     for column in dataFile_:    # each day
# #         date = column
# #         # print(dataFile_[column].tolist())
# #         colList = dataFile_[column].tolist()    # each day list of levels for different bins
        

# #         nodeList = []   # the bins that are to be emptied next day

# #         for i in range(len(colList)):   # iterating through levels of each bin
# #             if colList[i] + avg[i] > 100:
# #                 print()
# #                 nodeList.append(i)
# #                 avg[i] = 0
# #             else:
# #                 if i != 0:
# #                     currAvg = (colList[i] - colList[i - 1])/2   #error
# #                     avg[i] = avg[i] + currAvg
# #                 else:
# #                     avg[i] = colList[i]
# #         print(date, nodeList)
# #         # for nodeIndex in nodeList:
#         #     print(date, binCoordinates[nodeIndex + 1])


lis = [(1, 0), (2, 1)]
print(lis)
coord = (1, 0)
lis.remove(coord)
print(lis)
