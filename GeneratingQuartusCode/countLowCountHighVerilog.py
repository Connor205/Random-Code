from numpy import binary_repr


def main():
    """
    Goes through each line in the text document and formats it into a specific kind of
    case statement for verilog code
    """
    f = open("countLowCountHigh.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("output.txt", "w")
    # print(lines)
    current_val = 12
    for i, line in enumerate(lines):
        lines[i] = line.replace("\t", " ").replace("\n", "")
        vals = lines[i].split()  # Get all the values seperated by whitespace

        f.write("4'b" + binary_repr(i, 4) + ": begin\t\t//" + vals[0] + "\n")
        f.write("\ttimer = timer + 1'b1;\n")
        f.write("\tcountlow = " + str(int(float(vals[2]))) + ";\n")
        f.write("\tcounthigh = " + str(int(float(vals[3]))) + ";\n")
        f.write("\tsevensegLetter = 4'b" + binary_repr(current_val, 4) + ";\n")
        f.write("\tsevensegNumber = 4'b" + binary_repr(int(vals[0][1]), 4) +
                ";\n")
        f.write("\tif (timer > 50000000 * " + str(i + 1) + " ) begin\n")
        f.write("\t\tstate =  4'b" + binary_repr(i + 1, 4) + ";\n")
        f.write("\tend\nend\n")
        print(lines[i])
        current_val += 1  # increment the current value
        if current_val == 16:  # If G is reached
            current_val = 6  # G's should be displayed as 6s
        if current_val == 7:  # After 6 an A should be displayed
            current_val = 10


if __name__ == "__main__":
    main()
