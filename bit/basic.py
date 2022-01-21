def odd(n: int) -> bool:
    return bool(n & 1)

def same_sign(x: int, y: int) -> bool:
    # positive: 0...
    # negative: 1...
    return bool((x ^ y) >= 0)

def plus_one(n: int) -> int:
    # -n = ~n + 1
    return -~n

def minus_one(n: int) -> int:
    # -n = ~n + 1
    return ~-n

def swap(x: int, y: int) -> (int, int):
    # x ^ x = 0
    if x != y:
        x ^= y
        y ^= x
        x ^= y
    return x, y

def xor(x:int, y:int) -> int:
    return (x | y) - (x & y)

if __name__ == "__main__":
    n = 5
    print(f"Is {n} an odd number?", odd(n))
    n = 88
    print(f"Is {n} an odd number?", odd(n), end="\n\n")

    x, y = 1, 1
    print(f"Do {x} and {y} have the same sign?", same_sign(x, y))
    x, y = 1, -1
    print(f"Do {x} and {y} have the same sign?", same_sign(x, y))
    x, y = 7, 11
    print(f"Do {x} and {y} have the same sign?", same_sign(x, y), end="\n\n")

    n = 0
    print(f"{n} + 1 =", plus_one(n))
    n = -1
    print(f"{n} + 1 =", plus_one(n), end="\n\n")

    n = 0
    print(f"{n} - 1 =", minus_one(n))
    n = 1
    print(f"{n} - 1 =", minus_one(n), end="\n\n")

    x, y = 4, 4
    print((x, y), "->", swap(x, y))
    x, y = 9, 6
    print((x, y), "->", swap(x, y), end="\n\n")

    print(f'XOR of {x:b} and {y:b} is {xor(x, y):b}')