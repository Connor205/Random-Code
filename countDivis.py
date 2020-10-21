if __name__ == "__main__":
	currentCount = 0
	for x in range(500):
		val = x + 1
		if (val % 2 == 0 or val % 3 == 0 or val % 11 == 0):
			currentCount += 1
	print(currentCount)

  		