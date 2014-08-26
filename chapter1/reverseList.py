def reverseList(aList):
    lenOfaList = len(aList)
    if lenOfaList < 2:
        return
    swapMaxIndex = lenOfaList / 2 - 1
    count = 0
    while count <= swapMaxIndex:
        aList[count], aList[lenOfaList-count-1] = aList[lenOfaList-count-1], aList[count]
        count += 1
