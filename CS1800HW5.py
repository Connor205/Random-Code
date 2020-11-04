import sys
from itertools import *
def main():
  prob1A() 

# Python code to clone or copy a list
# Using the in-built function extend()
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

def prob1A():
  arr = [0,0,0,0]
  finalset = []
  sortedSet = []
  # print(arr)
  # Iterating through all possible combinations
  for i in range(0, 5):
    arr[0] = i
    for j in range(0,5):
      arr[1] = j
      for k in range(0,5):
        arr[2] = k
        for l in range(0, 5):
          arr[3] = l
          # print(arr)
          if sum(arr) == 5: # Check if the sum is equal to 5
            newArr = Cloning(arr)
            if newArr not in finalset: # add it if it is not already added
              finalset.append(Cloning(arr))
            newArr.sort()
            if newArr not in sortedSet:
              sortedSet.append(Cloning(arr))
  print("List off all combinations:\n", finalset) # Prints all possible working combinations
  print("Number of working combinations: ", len(finalset))
  print("List off all sorted combinations:\n", sortedSet) # Prints all possible working combinations

def prob2B(): # This will not run because there are some 20 trillion options it is here just for show.
  kobolds = list(range(1, 9))
  golbins = list(range(-8, 0))
  koboldOptions = list(permutations(kobolds, 8))
  golbinOptions = list(permutations(golbins, 8))
  arr = [0] * 16
  arrs = []
  for kob in koboldOptions:
    for gob in golbinOptions:
      for j in range(0,8):
        arr[2* j] = kob[j]
        arr[2 * j + 1] = gob[j]
        newArr = Cloning(arr)
        if newArr not in arrs:
          arrs.append(newArr)
  print(len(arrs))

# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)

    return l


def prob3():
  nums = []
  for i in range(0, 100000):
    strI = str(i)
    twos = strI.count("2")
    threes = strI.count("3")
    fours = strI.count("4")
    fives = strI.count("5")
    if (twos == 1 and threes == 1 and fours == 1 and fives == 1):
      nums.append(i)
  print(nums)
  print(len(nums))


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

def prob4():
  bucketCombos = list(sums(10, 7))
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  output = []
  #for i in "0123456789":
  for lines in bucketCombos:
    curentVal = 0
    newVal = 0
    string = ""
    for i in range(0, len(lines)):
      string += str(i)
      newVal = curentVal + lines[i]
      string += ''.join([str(elem) for elem in letters[curentVal:newVal]])
      curentVal = newVal
    string = string[1:]
    output.append(string)

    print(string)
  print(len(bucketCombos))
  print(len(output))

def prob6():
  count = 0
  for i in range(0,6):
    count += countP(5,i)
  print(count)

# Returns count of different partitions
# of n elements in k subsets
def countP(n, k):

    # Table to store results of subproblems
    dp = [[0 for i in range(k + 1)]
             for j in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(k + 1):
        dp[0][k] = 0

    # Fill rest of the entries in
    # dp[][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (j == 1 or i == j):
                dp[i][j] = 1
            else:
                dp[i][j] = (j * dp[i - 1][j] +
                                dp[i - 1][j - 1])

    return dp[n][k]


if __name__ == "__main__":
  main()

