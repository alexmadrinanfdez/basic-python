def roman_to_int(s: str) -> int:
    ri = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = 0
    for i in range(len(s)):
        n += ri[s[i]]
        if i > 0 and ri[s[i]] > ri[s[i-1]]:
            # subtract its value and revert the previous sum
            n -= 2 * ri[s[i-1]]
    
    return n

if __name__ == "__main__":
    s = "IV"
    print(s, "->", roman_to_int(s))
    s = "LVIII"
    print(s, "->", roman_to_int(s))
    s = "MCMXCIV"
    print(s, "->", roman_to_int(s))