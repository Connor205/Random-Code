import numpy as np

array = [["X", "O", ""],["X", "O", ""],["X", "O", ""]]
print(np.matrix(array))
print(array)

# There are two ways I would recommend doing this. 
# The first way is using numpy. 

#     input numpy as np
#     array = [["X", "O", ""],["X", "O", ""],["X", "O", ""]]
#     print(np.matrix(array))

# The second way would be to iterate through the entire board and print it

#     array = [["X", "O", ""],["X", "O", ""],["X", "O", ""]]
#     for row in array:
#       for val in row:
#         print(val, end="")
#       print() # This line adds a newline 
    





