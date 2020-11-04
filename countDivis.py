def listOfDivis(start: int, end: int, toInclude: list, toExclude: list):
    results = []
    for i in range(start, end + 1):
        include = False
        for inVal in toInclude:
            if i % inVal == 0:
                include = True
        for ex in toExclude:
            if i % ex == 0:
                include = False
        if include:
            results.append(i)
    return (len(results), results)


if __name__ == "__main__":
    includeA = [2, 3, 11]
    answerA = listOfDivis(1, 500, includeA, [])
    print(answerA[0])
    print(answerA[1])
