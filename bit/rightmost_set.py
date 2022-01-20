from math import log2

def unset(n):
    # n-1 flips every bit from the rightmost set (included)
    return n & (n-1)

def pow_two(n):
    return unset(n) == 0

def pos(n):
    # return log2(n & -n) + 1
    x = n ^ unset(n)
    return int(log2(x) + 1)

def parity_check(n):
    # amount of 1s in binary representation
    par = False
    while n:
        par = not par
        n = unset(n)
    return par

if __name__ == "__main__":
    n = 16
    print(f'{n} in binary is {bin(n)}')
    if pow_two(n):
        print("It is a power of two")
    else:
        print("It is not a power of two")
    print("The first '1' is at position", pos(n))
    if parity_check(n):
        print("Its parity is odd")
    else:
        print("Its parity is even")    