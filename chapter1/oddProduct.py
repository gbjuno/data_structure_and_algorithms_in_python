def oddProduct(aList):
    if len([element for element in aList if element % 2 != 0]) <= 1:
        return False
    else:
        return True
