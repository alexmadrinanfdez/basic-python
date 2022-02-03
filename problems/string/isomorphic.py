def is_isomorphic(s: str, t: str) -> bool:
    # Two strings `s` and `t` are isomorphic 
    # if the characters in `s` can be replaced to get `t`
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

if __name__ == "__main__":

    s, t = "add", "egg"
    print(f'Are "{s}" and "{t}" isomorphic?', end=' ')
    print(is_isomorphic(s, t))

    s, t = "paper", "house"
    print(f'Are "{s}" and "{t}" isomorphic?', end=' ')
    print(is_isomorphic(s, t))