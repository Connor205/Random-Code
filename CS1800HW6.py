import sys
from itertools import *


def main():
    prob2ii()


# Python code to clone or copy a list
# Using the in-built function extend()
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


def prob2i():
    # List of all ways to permute 9 numbers
    listOfPerms = list(permutations(range(1, 10), 9))
    listMatching = []
    for i in listOfPerms:
        if (i[2] + i[4] + i[6] == 6):
            listMatching.append(i)
    print(listMatching)
    matching = len(listMatching)
    total = len(listOfPerms)
    print(matching / total)
    return (matching / total)


def prob2ii():
    # List of all ways to permute 9 numbers
    listOfPerms = list(permutations(range(1, 10), 9))
    listMatching = []
    for i in listOfPerms:
        for j in range(0, 3):
            if i[0 + j * 3] + i[1 + j * 3] + i[2 + j * 3] == 6:
                listMatching.append(i)
            if i[j] + i[3 + j] + i[6 + j] == 6:
                listMatching.append(i)
        if (i[0] + i[4] + i[8] == 6):
            listMatching.append(i)
        if (i[2] + i[4] + i[6] == 6):
            listMatching.append(i)
    print(listMatching)
    matching = len(listMatching)
    total = len(listOfPerms)
    print(matching / total)
    return matching / total


def prob2iii():
    # List of all ways to permute the remaining 5 numbers numbers
    listOfPerms = list(permutations([1, 3, 6, 8, 9], 5))
    listMatching = []
    for i in listOfPerms:
        if (i[0] + i[4] == 4):
            listMatching.append(i)
    print(listMatching)
    matching = len(listMatching)
    print(matching)
    total = len(listOfPerms)
    print(total)
    print(matching / total)
    return matching / total


def prob4i():
    lessThan6 = []
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 + die2 <= 6:
                lessThan6.append((die1, die2))
    print(lessThan6)
    print(len(lessThan6))


if __name__ == "__main__":
    main()
