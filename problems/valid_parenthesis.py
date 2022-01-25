def is_valid_parenthesis(s):
    stack = []
    paren = ['(', ')', '[', ']', '{', '}']
    for char in s:
        if char in paren:
            idx = paren.index(char)
            # check there is an opening parenthesis
            if idx % 2 == 0:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                # check for matching parenthesis
                if stack.pop() != paren[idx-1]:
                    return False
        else:
            # allow other characters
            continue
    # unmatched parenthesis
    if stack:
        return False
    else:
        return True

if __name__ == "__main__":
    import sys
    try:
        s = sys.argv[1]
        if is_valid_parenthesis(s):
            print("Correct use of parenthesis.")
        else:
            print("There is an error in the use of parenthesis.")
    except IndexError:
        print("Usage: python", sys.argv[0], "'<phrase>'")