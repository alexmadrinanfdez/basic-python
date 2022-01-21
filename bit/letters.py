# ASCII codes
# ‘A’ — 01000001 ‘a’ — 01100001
# ‘B’ — 01000010 ‘b’ — 01100010
# ‘C’ — 01000011 ‘c’ — 01100011
# ‘D’ — 01000100 ‘d’ — 01100100
# ‘E’ — 01000101 ‘e’ — 01100101
# and so on...
# ' ' — 00100000
# '_' — 01011111

def lower_case(s: str) -> str:
    low = ''
    for c in s:
        # bitwise ops don't work with chr type
        low += chr(ord(c) | ord(' '))
    return low

def upper_case(s: str) -> str:
    up = ''
    for c in s:
        # bitwise ops don't work with chr type
        up += chr(ord(c) & ord('_'))
    return up

def invert_case(s: str) -> str:
    inv = ''
    for c in s:
        # bitwise ops don't work with chr type
        inv += chr(ord(c) ^ ord(' '))
    return inv

def alphabet_pos(c: chr) -> int:
    return ord(c) & 31

if __name__ == "__main__":
    s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    print("original:\t", s)
    print("lower:\t\t", lower_case(s))
    print("upper:\t\t", upper_case(s))
    print("inverted:\t", invert_case(s))
    for c in s:
        print(alphabet_pos(c), end=' ')