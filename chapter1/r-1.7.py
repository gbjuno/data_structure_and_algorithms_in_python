for i in [1,2,3,4,5,6,7,8,9,100]:
    print sum(x**2 for x in range(i) if x % 2 != 0)
