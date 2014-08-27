import sys,re

def wordCount(fileStr):
    wordCountDict = {}
    fileStr = 'i love programm, especially python progamming!\nThat is True!'
    print [repr(i) for i in re.split(r'\W+',fileStr)]
    for i in re.split(r'\W+',fileStr):
        if not i in wordCountDict:
            wordCountDict[i]=1
        else:
            wordCountDict[i] += 1
    print wordCountDict

def main(filename):
    with open(filename) as filehandler:
        fileStr = filehandler.read()
    wordCount(fileStr)

if __name__ == '__main__':
    main(sys.argv[1])
