#imports
from sympy import *

#val declarations
numX = 1
valX = 1
numY = 1
valY = 1
xyTotal = 1
valTotal = 1

def simplifyXY(xyTotal):
    return 'x = xyTotal - y'

def findX(numX, numY, valTotal):
    #lol

def findY(numX, valX, numY, valTotal):
    #lol

if __name__ == '__main__':

    xyTotal = input('Input the sum of x and y: ')
    numX = input('How many x?: ')
    numY = input('How many y?: ')
    valTotal = input('Totalling to...?: ')

    valX = findX(numX, numY, valTotal)
    valY = findY(numX, valX, numY, valTotal)