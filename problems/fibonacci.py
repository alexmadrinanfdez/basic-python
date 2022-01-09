def recursive_fib(n):
    "Returns the nth number of the Fibonacci series."
    if n < 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

def fib(n):
    "Writes the Fibonacci series up to 'n'."
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print() # new line

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))