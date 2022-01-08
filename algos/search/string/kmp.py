def longest_prefix_suffix(pat):
    lps = [0] * len(pat)
    pre = 0
    # preprocess the pattern
    for i in range(1, len(pat)):
        # roll the prefix pointer back until match or 
        # beginning of pattern is reached
        while pre and pat[i] != pat[pre]:
            pre = lps[pre-1]
        # if match, record the LSP for the current `i`
        # and move prefix pointer
        if pat[i] == pat[pre]:
            pre += 1
            lps[i] = pre
    return lps

def kmp_match(txt, pat):
    pos = []
    idx = 0
    # Knuth-Morris-Pratt algorithm
    lps = longest_prefix_suffix(pat)
    for i, ch in enumerate(txt):
        # if a mismatch was found, roll back the pattern
        # index using the information in LPS
        while idx and pat[idx] != ch:
            idx = lps[idx-1]
        # if match
        if pat[idx] == ch:
            # if the end of a pattern is reached, record a result
            # and use infromation in LSP array to shift the index
            if idx == len(pat)-1:
                pos.append(i - idx)
                idx = lps[idx]
            else:
                idx += 1
    return pos
  
if __name__ == "__main__":
    s = "The building fronts are just fronts, to hide the people watching."
    print(s)

    sub = "front"
    match = kmp_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )
    sub = "hi"
    match = kmp_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )