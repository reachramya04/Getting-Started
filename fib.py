#recursive approach
numTerms = int(input("How many terms of fibonacci sequence to print? "))

# What are the first few terms of the fib seq?
# 0 1 1 2 3

# main method
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

# check if the number of terms is valid
if numTerms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(numTerms):
        print(fibonacci(i))
