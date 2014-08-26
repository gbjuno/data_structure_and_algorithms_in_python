def countVowels(aStr):
    vowelsStr='aeiou'
    countVowels = 0
    for i in aStr:
        if i in vowelsStr:
            countVowels += 1
    return countVowels
