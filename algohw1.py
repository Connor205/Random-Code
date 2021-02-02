def createList(startingString):
    output = []
    for i in startingString:
        output.append(True if i == '1' else False)
    return output


def generateBinaryStringSolution(binaryString):
    ones = binaryString.count(True)
    if ones % 2 == 0:
        print("failed")
        return False
    if len(binaryString) == 1:
        return [0]
    first = binaryString.index(True)
    toReturn = [first]
    if first != 0:
        binaryString[first - 1] = not binaryString[first - 1]
        ## print(binaryString[:first])
        toReturn += (generateBinaryStringSolution(binaryString[:first]))
    if first != len(binaryString) - 1:
        binaryString[first + 1] = not binaryString[first + 1]
        ## print(binaryString[first + 1:])
        toReturn += [
            x + first + 1
            for x in (generateBinaryStringSolution(binaryString[first + 1:]))
        ]
    return toReturn


testingString = "10000101"
testingString2 = "11111111111"
testList = createList(testingString2)
print(generateBinaryStringSolution(testList))