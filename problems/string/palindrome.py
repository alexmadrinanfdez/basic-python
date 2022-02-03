def is_palindrome(s):
    # remove non alphanumeric characters
    an = ""
    for char in s:
        if char.isalnum():
            an += char.lower()
    # check for palindrome
    return an == an[::-1]

if __name__ == "__main__":

    s = "A man, a place, a canal: Panama."
    print(f"Is the string '{s}' a palindrome?", end=' ')
    print(is_palindrome(s))

    s = "A man, a plan, a canal: Panama."
    print(f"Is the string '{s}'a palindrome?", end=' ')
    print(is_palindrome(s))