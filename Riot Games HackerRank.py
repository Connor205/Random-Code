#!/bin/python3

import math
import os
import random
import re
import sys


import fileinput
# Complete the 'PrintGardenLayout' function below.

def PrintGardenLayout():
    # Write your code here
    lineNum = 0
    for line in fileinput.input():
        if (lineNum == 0):
            comma = line.index(',')
            x = int(line[0:comma])
            y = int(line[comma+1:len(line)])
            garden = [['B' for i in range(x)] for j in range(y)]
        else:
            firstComma = line.index(',')
            numbers = line[firstComma + 1: len(line)]
            secondComma = numbers.index(',')
            yCoord = numbers[0:secondComma]
            xCoord = numbers[secondComma + 1: len(numbers)]
            garden[int(xCoord)][int(yCoord)] = line[0]
        lineNum += 1
    for row in garden:
        s = ""
        for value in row:
            s+= value
        print (s)

#!/bin/python3


# Complete the 'PrintGardenLayoutWithIdealSeats' function below.

def PrintGardenLayoutWithIdealSeats():
    # Write your code here
    # Creating Garden
    lineNum = 0
    for line in fileinput.input():
        if (lineNum == 0):
            comma = line.index(',')
            x = int(line[0:comma])
            y = int(line[comma+1:len(line)])
            garden = [['B' for i in range(x)] for j in range(y)]
        else:
            firstComma = line.index(',')
            numbers = line[firstComma + 1: len(line)]
            secondComma = numbers.index(',')
            yCoord = numbers[0:secondComma]
            xCoord = numbers[secondComma + 1: len(numbers)]
            garden[int(xCoord)][int(yCoord)] = line[0]
        lineNum += 1
    flowersSeen = [[0 for i in range(x)] for j in range(y)]
    filled = False

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            count = 0
            if (garden[i][j] == 'B'):
                #Count Number of Flowers Seen
                #To Left
                walled = False
                for k in range(i + 1):
                    if (not walled):
                        if(garden[i-k][j] == 'F'):
                            count +=1
                        if (garden[i-k][j] == 'W'):
                            walled = True
                #To Right
                walled = False
                for k in range(len(garden[0]) - i - 1):
                    if (not walled):
                        if(garden[i+k][j] == 'F'):
                            count +=1
                        if (garden[i+k][j] == 'W'):
                            walled = True
                #Above
                walled = False
                for k in range(j + 1):
                    if (not walled):
                        if (garden[i][j-k] == 'F'):
                            count+= 1
                        if (garden[i][j-k] == 'W'):
                            walled = True     
                #Below
                for k in range(len(garden) - j - 1):
                    if (not walled):
                        if (garden[i][j+k] == 'F'):
                            count+= 1
                        if (garden[i][j+k] == 'W'):
                            walled = True 
                flowersSeen[i][j] = count
            else:
                flowersSeen[i][j] = -1
    # Find Max Number of Flowers Seen
    maxFlowers = 0
    for row in flowersSeen:
        for value in row:
            if (value > maxFlowers):
                maxFlowers = value
    # Filing Garden
    if (maxFlowers != -1):
        for i in range(len(flowersSeen)):
            for j in range(len(flowersSeen[0])):
                if (flowersSeen[i][j] == maxFlowers):
                    garden[i][j] = '*'
    # Printing Final Garden
    for row in garden:
        s = ""
        for value in row:
            s+= str(value)
        print (s)

if __name__ == '__main__':

if __name__ == '__main__':
