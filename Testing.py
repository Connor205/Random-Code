def print_fib():
    """This function prints the fib sequence for 100 digits.
    """
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(100 - 2):
        fib_list.append(fib_list[i] + fib_list[i + 1])
        print(fib_list)


if __name__ == '__main__':
    print_fib()
