def main():
    f = open("toScrape.txt", "r")
    lines = f.readlines()
    strOutput = {}
    currentIndex = ""
    for i, line in enumerate(lines):
        line = line.replace("\t",
                            "").replace(" ", "").replace("\n", "").replace(
                                "+", "").replace("\\", "").replace("&=", "")
        line = line[:-2]
        if not line[0].isdigit():
            currentIndex = line[0]
            line = line[1:]
            strOutput[currentIndex] = []
        line = line.replace("0", "(D[0] & ")
        line = line.replace("1", "D[1] & ")
        line = line.replace("2", "D[2] & ")
        line = line.replace("3", "D[3])")
        line = line.replace("(D[0] & '", "(~D[0] & ")
        line = line.replace("D[1] & '", "~D[1] & ")
        line = line.replace("D[2] & '", "~D[2] & ")
        line = line.replace("D[3])'", "~D[3])")
        strOutput[currentIndex].append(line)

        lines[i] = line

    for index, key in enumerate(strOutput.keys()):
        listToStr = ' | '.join(map(str, strOutput[key]))
        listToStr = "assign sevenoutputs[" + str(
            index) + "] = ~(" + listToStr + ");"
        print(listToStr)


if __name__ == "__main__":
    main()
