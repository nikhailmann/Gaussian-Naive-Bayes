import math


def GuassineFormula(inputXValue, inputYValue, meanMatrix, varianceMatrix,
                    classNum):
    inputXValue = float(inputXValue)
    inputYValue = float(inputYValue)
    probabilityOfClass = matrixofdatapoints[classNum] / totaldatapoints
    probabilityOfXValue = (
        1 /
        (math.sqrt(2 * math.pi * varianceMatrix[classNum * 2]))) * math.pow(
            math.e, -1 * ((inputXValue - meanMatrix[classNum * 2])**2) /
            (2 * varianceMatrix[classNum * 2]))
    probabilityOfYValue = (1 / (math.sqrt(
        2 * math.pi * varianceMatrix[classNum * 2 + 1]))) * math.pow(
            math.e, -1 * ((inputYValue - meanMatrix[classNum * 2 + 1])**2) /
            (2 * varianceMatrix[classNum * 2 + 1]))
    endProbability = probabilityOfClass * probabilityOfXValue * probabilityOfYValue
    return endProbability


def calculateMetrics(matrix):
    mean = calculateMean(matrix)
    variance = calculateVariance(matrix)
    return mean, variance


def calculateMean(matrix):
    sum = 0
    for num in matrix:
        sum += num
    mean = sum / len(matrix)
    return mean


def calculateVariance(matrix):
    mean = calculateMean(matrix)
    varsum = 0
    for num in matrix:
        varsum += (num - mean)**2
    variance = varsum / (len(matrix) - 1)
    return variance


f = open("data.txt", "r")
data = f.read().splitlines()
f.close()
for i in range(0, len(data)):
    data[i] = data[i].split()
    data[i] = list(map(float, data[i]))
totaldatapoints = 2 * len(data)
matrixofdatapoints = []
currentclass = 0
matrixofmeanvals = []
matrixofvariancevals = []
matrixXvals = []
matrixYvals = []
sumofdatapoints = 0
for i in range(0, len(data)):
    next = True
    notatEnd = True
    if i + 1 == len(data):
        notatEnd = False

    if notatEnd and (data[i + 1][0] != currentclass):
        next = False

    if data[i][0] == currentclass:
        matrixXvals.append(data[i][1])
        matrixYvals.append(data[i][2])
        sumofdatapoints += 2

    if not next or i + 1 == len(data):
        meanX, varianceX = calculateMetrics(matrixXvals)
        meanY, varianceY = calculateMetrics(matrixYvals)
        matrixofmeanvals.append(meanX)
        matrixofmeanvals.append(meanY)
        matrixofvariancevals.append(varianceX)
        matrixofvariancevals.append(varianceY)
        matrixXvals.clear()
        matrixYvals.clear()
        currentclass += 1
        matrixofdatapoints.append(sumofdatapoints)
        sumofdatapoints = 0

XValue = input("Enter X Value: ")
YValue = input("Enter Y Value: ")
for i in range(0, currentclass):
    classNum = i
    probability = GuassineFormula(XValue, YValue, matrixofmeanvals,
                                  matrixofvariancevals, classNum)
    print("Class " + str(classNum) + " probability: " + str(probability))
