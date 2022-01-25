def rabin_karp_match(txt, pat):
    M = len(pat)
    N = len(txt)
    d = 256 # number of characters in the input alphabet
    q = 101 # prime number
    p = 0   # hash value for pattern 
    t = 0   # hash value for input text
    pos = []
    # Rabin-Karp algorithm
    h = d**(M-1) % q
    # hash value of pattern and first window of text 
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q
    # slide the pattern over text one by one 
    for i in range(N - M+1):
        # check the hash values of current window of text and pattern
        # if the hash values match then only...
        if p == t: 
            # ...check for characters (one by one)
            if pat == txt[i:i+M]:
                pos.append(i)
  
        # calculate hash value for next window of text:
        # remove leading digit, add trailing digit
        if i < N-M: 
            t = (d * (t-ord(txt[i]) * h) + ord(txt[i+M])) % q
            # it might result in negative values of t
            if t < 0:
                t = t + q
    return pos

if __name__ == "__main__":
    s = "The building fronts are just fronts, to hide the people watching."
    print(s)

    sub = "front"
    match = rabin_karp_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )
    sub = "ing"
    match = rabin_karp_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )