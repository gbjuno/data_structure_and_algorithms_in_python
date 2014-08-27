from random import randint
import sys

def birthParadox(numOfPeople):
    testCount = 1000000
    goodCaseCount = 0
    badCaseCount = 0
    for testIndex in range(testCount):
        testResult = []
        for indexOfPeople in range(numOfPeople):
            resultOfIndexPeople = randint(1,366)
            if resultOfIndexPeople in testResult: 
                goodCaseCount += 1
                break
            testResult.append(resultOfIndexPeople)
        if len(testResult) == numOfPeople: badCaseCount += 1
    print "result: %s goodcases, %s badcases" % (goodCaseCount,badCaseCount)
    print "probability: %s" % str(float(goodCaseCount)/testCount)

birthParadox(int(sys.argv[1]))
