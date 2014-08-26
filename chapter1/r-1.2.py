def is_even(k):
    if not isinstance(k,int):
        raise TypeError('%s is not integer' % k)
    else:
        strk = str(k)
        if strk[-1] in "02468":
            return True
        else:
            return False

testCase = [100,101,42,44,56,58,57,43,32.1,'40','39']
for i in testCase:
    try:
        if is_even(i):
            print "%s is even" % i
        else:
            print "%s is not even" % i
    except TypeError,e:
        print e

