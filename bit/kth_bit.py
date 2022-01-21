def on(n, k):
    # no bits except kth set: 1 << (k-1)
    return n | (1 << (k-1))

def off(n, k):
    # all bits except kth set: ~(1 << (k-1))
    return n & ~(1 << (k-1))

def check(n, k):
    # no bits except kth set: 1 << (k-1)
    return (n & (1 << (k-1))) != 0

def toggle(n, k):
    # no bits except kth set: 1 << (k-1)
    return n ^ (1 << (k-1))

def binary_repr(n: int, l:int=32) -> str:
    b = ''
    i = 1 << l-1
    # check bits one by one
    while i > 0:
        b += '1' if (n & i) else '0'
        i //= 2
    return b

if __name__ == "__main__":
    n, k = 11, 3
    print(f'{n} in binary is {n:#b}')
    print(f'Turning {k}\'th bit on...')
    n = on(n, k)
    print(f'{n} in binary is {n:#b}', end="\n\n")
    
    print(f'{n} in binary is {n:#b}')
    print(f'Turning {k}\'th bit off...')
    n = off(n, k)
    print(f'{n} in binary is {n:#b}', end="\n\n")

    print(f'{n} in binary is {n:#b}')
    if check(n, k):
        print(f'{k}\'th bit is set')
    else:
        print(f'{k}\'th bit is not set')
    print()

    print(f'{n} in binary is {n:#b}')
    print(f'Toggling {k}\'th bit...')
    n = toggle(n, k)
    print(f'{n} in binary is {n:#b}', end="\n\n")

    print("Binary representation of numbers in memory uses 32 bits")
    print(f'Therefore, {n} is stored as {binary_repr(n)}')