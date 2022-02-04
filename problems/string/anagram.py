def is_anagram(s: str, t: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1
        # all frequencies should be zero
        return not any(freq.values())

if __name__ == "__main__":
    s, t = "add", "dad"
    print(f'Are "{s}" and "{t}" anagrams?', end=' ')
    print(is_anagram(s, t))

    s, t = "paper", "raper"
    print(f'Are "{s}" and "{t}" anagrams?', end=' ')
    print(is_anagram(s, t))