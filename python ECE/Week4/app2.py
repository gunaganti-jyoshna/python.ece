#Addition
# importing numpy as np
import numpy as np
# creating first matrix
A = np.array([[1, 2], [3, 4]])
# creating second matrix
B = np.array([[4, 5], [6, 7]])
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))
 
#Substraction
# importing numpy as np
import numpy as np
# creating first matrix
A = np.array([[1, 2], [3, 4]])
# creating second matrix
B = np.array([[4, 5], [6, 7]])
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
# subtracting two matrix
print("Subtraction of two matrix")
print(np.subtract(A, B))

# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
# 3x3 matrix

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
# 3x4 matrix

# Result matrix (3x4) initialized to zero
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# Iterate through rows of X
for i in range(len(X)):
    # Iterate through columns of Y
    for j in range(len(Y[0])):
        # Iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

# Print the result matrix
for r in result:
    print(r)

