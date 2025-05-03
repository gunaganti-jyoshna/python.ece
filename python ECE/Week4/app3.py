import numpy as np

# Initializing variables
x1 = 0
x2 = 0
x3 = 0
epsilon = 0.01  # Convergence tolerance
converged = False
x_old = np.array([x1, x2, x3])  # Storing the old values of x1, x2, x3

print('Iteration results')
print(' k, x1, x2, x3 ')

# Iterating up to 50 times
for k in range(1, 50):
    # Gauss-Seidel Iteration
    x1 = (14 - 3*x2 + 3*x3) / 8
    x2 = (5 + 2*x1 - 5*x3) / (-8)
    x3 = (-8 - 3*x1 - 5*x2) / (-5)
    
    # Create an array of current values for x1, x2, x3
    x = np.array([x1, x2, x3])
    
    # Calculate the change between the old and new solutions (Euclidean distance)
    dx = np.sqrt(np.dot(x - x_old, x - x_old))
    
    # Print the current iteration and values of x1, x2, x3
    print("%d, %.4f, %.4f, %.4f" % (k, x1, x2, x3))
    
    # If the change is smaller than epsilon, stop and declare convergence
    if dx < epsilon:
        converged = True
        print('Converged!')
        break
    
    # Update old values of x1, x2, x3 for the next iteration
    x_old = x

# If not converged within 50 iterations, print a message
if not converged:
    print('Not converge, increase the # of iterations')
