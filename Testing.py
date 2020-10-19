def printFib():
  FibList = []
  FibList.append(0)
  FibList.append(1)
  for i in range(100 - 2):
    FibList.append(FibList[i] + FibList[i + 1])
    print(FibList)
# print(len(FibList))

if __name__ == '__main__':
  printFib()
