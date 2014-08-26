from random import randint
def shuffle(aList):
    shuffCount = len(aList) - 1
    while shuffCount >= 0:
        aList.append(aList.pop(randint(0,shuffCount)))
        shuffCount -= 1

        
