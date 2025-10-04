# Even/Odd and Prime Number Checker

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get input from user
num = int(input("Enter a number: "))

# Check even or odd
if is_even(num):
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

# Check prime
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")

