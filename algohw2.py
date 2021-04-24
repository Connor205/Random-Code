import numpy as np
import math


def main():
    problem3D("homework", "workhome")


# Simple operation doing method that takes in two numbers and a string operator
def doOperation(n1, op, n2):
    if op == "*":
        return n1 * n2
    if op == "-":
        return n1 - n2
    if op == "+":
        return n1 + n2


def problem2C():
    inputL = [int(x) for x in "1 2 3 4 5".split()]  # Can be any list of ints
    ops = ['+', "*", '+', "*"]
    if len(ops) != len(inputL) - 1:  # Deals with invalid number of operatiors
        exit(0)

    l = len(inputL)

    # Creates two arrays for mins and maxes
    mins = [[math.inf] * l] * l
    maxes = [[-math.inf] * l for _ in range(l)]

    # Fills the arrays with the default values down the middle
    for i in range(l):
        mins[i][i] = maxes[i][i] = inputL[i]

    # Iterate through all of the diagonals
    for diag in range(2, l + 1):

        for i in range(l - diag + 1):
            j = i + diag - 1
            row = i
            col = j
            # Iterate through all possible splits for the given row and col
            for k in range(row, col):
                # Check to see if any possible values are the maximum and set it to the max at that position
                maxes[row][col] = max(
                    maxes[row][col],  # To prevent overwriting 
                    doOperation(maxes[row][k], ops[k], maxes[k + 1][col]),
                    doOperation(mins[row][k], ops[k], mins[k + 1][col]),
                    doOperation(maxes[row][k], ops[k], mins[k + 1][col]),
                    doOperation(mins[row][k], ops[k], maxes[k + 1][col]))
                # Check to see if any possible values are the minimum and set it to the min at that position
                mins[row][col] = min(
                    mins[row][col],
                    doOperation(maxes[row][k], ops[k], maxes[k + 1][col]),
                    doOperation(mins[row][k], ops[k], mins[k + 1][col]),
                    doOperation(maxes[row][k], ops[k], mins[k + 1][col]),
                    doOperation(mins[row][k], ops[k], maxes[k + 1][col]))
    return maxes[0][-1]  # Returns the biggest possible value


def problem3C(s1, s2):
    if len(s1) != len(s2):
        exit(0)
    #Create an array n + 1 by n + 1
    n = len(s1)
    grid = [[None] * (n + 1) for _ in range(n + 1)]
    # Iterate over the grid column by column starting from the right
    for col in range(n + 1):
        for row in range(n + 1):
            #Fills in first row and col of all 0s
            if col == 0 or row == 0:
                grid[row][col] = 0
            # Check to see if the two characters are equal
            elif s1[col - 1] == s2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
    #Starting string and staring indicies
    s = ""
    a = b = 0
    # Iterate until we reach the bottom right of the table
    while a < n and b < n:
        #If they match add them and then increment a and b
        if s1[a] == s2[b]:
            s = s + s1[a]
            a += 1
            b += 1
        # If we should go down then go down
        elif grid[a + 1][b] > grid[a][b + 1]:
            a += 1
        # Otherwise go right
        else:
            b += 1
    # Return final result
    return s


def problem3D(s1, s2):
    if len(s1) != len(s2):
        exit(0)
    #Create two arrays of size n
    n = len(s1)
    previous = [None] * (n + 1)
    current = [None] * (n + 1)
    # Iterate over the grid column by column starting from the right
    for col in range(n + 1):
        for row in range(n + 1):
            #Fills in first row and col of all 0s
            if col == 0 or row == 0:
                current[row] = 0
            # Check to see if the two characters are equal
            elif s1[col - 1] == s2[row - 1]:
                current[row] = previous[row - 1] + 1
            else:
                current[row] = max(previous[row], current[row - 1])
        # Reuse the given space and reset the current row
        previous = current.copy()
        current = [None] * (n + 1)
    return previous[-1]


if __name__ == "__main__":
    main()