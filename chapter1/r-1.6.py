def sumSquaresOfOddIntLt(n):
    sumSquaresOfOddInt = 0
    for i in range(n):
        if i % 2 != 0:
            sumSquaresOfOddInt += i**2
    return sumSquaresOfOddInt

for i in [1,2,3,4,5,6,7,8,9,100]:
    print sumSquaresOfOddIntLt(i)
