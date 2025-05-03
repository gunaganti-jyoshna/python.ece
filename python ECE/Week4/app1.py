#a) Creating a matrix of given order m x n containing random numbers in the range 1 to 99999
import numpy as np

def create_random_matrix(m, n):
    matrix = np.random.randint(1, 100000, size=(m, n))
    return matrix

# Example usage:
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

random_matrix = create_random_matrix(m, n)
print("Generated Random Matrix:")
print(random_matrix)
