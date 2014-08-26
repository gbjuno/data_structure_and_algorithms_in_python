def sumSquaresOfIntlt(n):
    if n <= 0:
        raise ValueError("%s is not a positive integer"%n)
    elif not isinstance(n,int):
        raise TypeError("%s is not a integer"%n)

#    startInt = 1
    sumSquaresOfInt = 0
#    while startInt < n:
#        sumSquaresOfInt += startInt ** 2
#        startInt+=1
    for i in xrange(n):
        sumSquaresOfInt += i**2
    return sumSquaresOfInt

testcase = [3,4,5,6,7,100,-12,1.3]
for i in testcase:
    try:
        sumSquaresOfInt = sumSquaresOfIntlt(i)
        print "sumSquaresofInt less than %s is %s" % (i,sumSquaresOfInt)
    except (ValueError,TypeError),e:
        print e

    
