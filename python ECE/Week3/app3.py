#c)Write a function collatz(x) which does the following: if x is odd 
#x = 3x + 1; if x is even,then x = x/2. Return the number of steps it
#takes for x = 1
def collatz(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2  # Use integer division to avoid float
        else:
            x = 3 * x + 1
        steps += 1
    return steps
n = int(input("Enter a number: "))
print(f"It took {collatz(n)} steps to reach 1.")
