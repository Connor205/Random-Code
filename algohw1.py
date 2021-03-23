"""
The code contained for solving the binary string breakdown problem for CS3000hw1. 
It is currently fully functional and contains an optimal solution.
"""


def createList(startingString):
    """Converts a string of 1's and 0's to a list of booleans

    Args:
        startingString (str): the string to be converted

    Returns:
        [bool]: the list of booleans
    """
    output = []
    for i in startingString:
        output.append(True if i == '1' else False)
    return output


def generateBinaryStringSolution(binaryString):
    """Generates the series of steps used to collapse a given binary string.

    Args:
        binaryString ([bool]): The binary string to be collapsed 

    Returns:
        [int]: A list of ints representing the moves in order from left to right
    """
    ones = binaryString.count(True)
    if ones % 2 == 0:
        print("failed")
        return False
    if len(binaryString) == 1:
        return [0]
    first = binaryString.index(True)
    to_return = [first]
    if first != 0:
        binaryString[first - 1] = not binaryString[first - 1]
        ## print(binaryString[:first])
        to_return += (generateBinaryStringSolution(binaryString[:first]))
    if first != len(binaryString) - 1:
        binaryString[first + 1] = not binaryString[first + 1]
        ## print(binaryString[first + 1:])
        to_return += [
            x + first + 1
            for x in (generateBinaryStringSolution(binaryString[first + 1:]))
        ]
    return to_return


def main():
    testingString = "10000101"
    testingString2 = "11111111111"
    testList = createList(testingString2)
    print(generateBinaryStringSolution(testList))
