def minmax(data):
    if data:
        minData,maxData = data[0],data[0]
        for i in data:
            if minData > i:
                minData = i
            elif maxData < i:
                maxData = i
        return minData,maxData
    else:
        raise ValueError("data sequence is empty")

testcase = [13,356,87,2,3,567,2333]
try:
    print testcase
    min,max = minmax(testcase)
    print "min = %s, max = %s" % (min,max)
except ValueError,e:
    print e
