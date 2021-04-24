import math


def main():
    print(problem4B())


# Opt(i) = Max(opt(i - 1), prices(i) + opt(t))
# Where t is the biggest value < i where prices(t) < prices(i) and opt(t - 1) < opt(t)

# OPT(i) = Max(opt(i - 1),


def problem4B():
    prices = [int(x) for x in "4 1 2 5".split()]
    print(prices)

    l = len(prices)
    best = [None] * (l)
    bestInc = [None] * (l)
    best[0] = prices[0]
    bestInc[0] = prices[0]

    for i in range(1, l):
        previous = best[i - 1]
        print("Previous: " + str(previous))
        currentPrice = prices[i]
        print("Current Value: " + str(currentPrice))
        j = i - 1
        toAdd = 0
        for j in range(i):
            if prices[j] <= currentPrice:
                toAdd = max(toAdd, bestInc[j])
        bestInc[i] = toAdd + currentPrice
        best[i] = max(previous, bestInc[i])

        print(best)
        print(bestInc)

    return best[-1]


if __name__ == "__main__":
    main()