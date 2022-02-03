def count_primes(n: int) -> int:
    """
    return the number of prime numbers that are less than `n`
    """
    if n < 3:
        return 0
    # sieve of Eratosthenes
    sieve = [1] * n
    sieve[0] = sieve[1] = False
    i = 2
    while i * i < n:
        if sieve[i]:
            sieve[i*i:n:i] = [0] * len(sieve[i*i:n:i])
        i += 1 if i == 2 else 2
    return sum(sieve)

if __name__ == "__main__":
    import sys
    
    try:
        x = int(sys.argv[1])
        y = count_primes(x)
        print(f'There are {y} prime numbers below {x}')
    except IndexError:
        print("Usage: python", sys.argv[0], "<number>")