def bad_char_heuristic(string, size):
    d = 256 # number of characters in the input alphabet
    bad_char = [-1] * d
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char

def boyer_moore_match(txt, pat):
    M = len(pat)
    N = len(txt)
    pos = []
    # Boyer Moore algorithm
    bad_char = bad_char_heuristic(pat, M)
    s = 0 # shift of the pattern with respect to text
    while s <= N - M:
        j = M-1
        # keep reducing index j of pattern while
        # characters of pattern and text are matching
        while j > -1 and pat[j] == txt[s + j]:
            j -= 1
        # if the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            pos.append(s)
            # Shift the pattern so that the next character in text
            # aligns with the last occurrence of it in pattern.
            # The condition s + m < n is necessary for the case when
            # pattern occurs at the end of text
            s += (M - bad_char[ord(txt[s + M])] if s + M < N else 1)
        else:
            # Shift the pattern so that the bad character in text
            # aligns with the last occurrence of it in pattern. The
            # max function is used to make sure that we get a positive
            # shift. We may get a negative shift if the last occurrence
            # of bad character in pattern is on the right side of the
            # current character.
            s += max(1, j - bad_char[ord(txt[s + j])])
    return pos

if __name__ == "__main__":
    s = "The building fronts are just fronts, to hide the people watching."
    print(s)

    sub = "front"
    match = boyer_moore_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )
    sub = "ing"
    match = boyer_moore_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )