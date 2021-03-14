import random

def ListToString(InputList):
    return ''.join(InputList)

# Given a list of strings, this function will return a list of indices in which the elements which only contain a space
# i.e: [' ','B','C',' '] -> [0,3]
def GetEmptyCells(InputList):
    return [ i for i in range(len(InputList)) if InputList[i] == ' ' ]


# Given a list, return an element from that list chosen at random
def GetRandomElement(InputList):
    n = len(InputList)
    # Length - 1 because we index from 0
    Index = random.randint(0,n-1)
    return InputList[Index]

def MaxIndices(InputList):
    return  [ i for i in range(len(InputList)) if InputList[i] == max(InputList) ]