import timeit


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


def testBinaryString():
    testingString2 = "0" * 50 + "1" + "0" * 50 + "11"
    testList = createList(testingString2)
    start = timeit.default_timer()
    print(generateBinaryStringSolution(testList))

    stop = timeit.default_timer()

    print('Time: ', stop - start)


def generateValuesForSpyNetwork(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    return n + generateValuesForSpyNetwork(
        n / 2) + generateValuesForSpyNetwork(n - n / 2)


def testSpy():
    for i in [2, 4, 8, 16, 32, 64]:
        print(generateValuesForSpyNetwork(i))


def main():
    testSpy()


if __name__ == "__main__":
    main()
