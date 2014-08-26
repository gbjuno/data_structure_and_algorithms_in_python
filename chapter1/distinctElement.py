def distinctElement(aList):
    lenOfaList = len(aList)
    count = 0
    while count < lenOfaList:
        if aList[count] in aList[0:count]:
            return False
        count+=1
    return True
