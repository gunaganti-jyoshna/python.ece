#b) Printing all the primes less than a given number
def is_prime(MyNum):
    if MyNum < 2:
        return False
    for i in range(2, MyNum // 2 + 1):
        if MyNum % i == 0:
            return False
    return True

def print_primes_less_than(x):
    print(f"Prime numbers less than {x} are:")
    for i in range(2, x):
        if is_prime(i):
            print(i, end=" ")

# Call the function to print primes less than 50
print_primes_less_than(90)
