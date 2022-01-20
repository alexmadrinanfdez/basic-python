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

if __name__ == "__main__":
    n, k = 11, 3
    print(f'{n} in binary is {bin(n)}')
    print(f'Turning {k}\'th bit on...')
    n = on(n, k)
    print(f'{n} in binary is {bin(n)}', end="\n\n")
    
    print(f'{n} in binary is {bin(n)}')
    print(f'Turning {k}\'th bit off...')
    n = off(n, k)
    print(f'{n} in binary is {bin(n)}', end="\n\n")

    print(f'{n} in binary is {bin(n)}')
    if check(n, k):
        print(f'{k}\'th bit is set')
    else:
        print(f'{k}\'th bit is not set')
    print()

    print(f'{n} in binary is {bin(n)}')
    print(f'Toggling {k}\'th bit...')
    n = toggle(n, k)
    print(f'{n} in binary is {bin(n)}')