def brute_force_match(txt, pat):
    if len(txt) < len(pat):
        return -1
    pos = []
    # compare the pattern at every feasible position
    for i in range(0, len(txt) - len(pat)):
        if pat == txt[i:i+len(pat)]:
            pos.append(i)
    return pos

if __name__ == "__main__":
    s = "The building fronts are just fronts, to hide the people watching."
    print(s)

    sub = "front"
    match = brute_force_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )
    sub = "hi"
    match = brute_force_match(s, sub)
    print(
        "The substring '{}' is present at {} position(s): {}."
        .format(sub, len(match), match)
    )