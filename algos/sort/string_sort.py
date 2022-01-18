def _char_counts(string):
    size = 256 # ASCII
    cnts = [0] * size
    for char in string.replace(' ', ''):
        cnts[ord(char)] += 1
    return cnts

def string_sort(string):
    cnts = _char_counts(string)
    res = ""
    for i, n in enumerate(cnts):
        res += chr(i) * n
    return res

if __name__ == "__main__":
    s = "the quick brown fox jumps over the lazy dog"
    print(s, "->", string_sort(s))