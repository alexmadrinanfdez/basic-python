def is_palindrome(s):
    # remove non alphanumeric characters
    an = ""
    for char in s:
        if char.isalnum():
            an += char.lower()
    # check for palindrome
    return an == an[::-1]

def longest_palindrome(s: str) -> str:
    # get the longest palindrome substring
    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        res = max(helper(s, i, i), helper(s, i, i+1), res, key=len)
    return res

if __name__ == "__main__":

    s = "A man, a place, a canal: Panama."
    print(f'Is the string "{s}" a palindrome?', end=' ')
    print(is_palindrome(s))

    s = "A man, a plan, a canal: Panama."
    print(f'Is the string "{s}" a palindrome?', end=' ')
    print(is_palindrome(s))

    s = "Let's attack the substring problem!"
    print(f'Which is the biggest palindrome inside "{s}"?', end=' ')
    print(longest_palindrome(s))