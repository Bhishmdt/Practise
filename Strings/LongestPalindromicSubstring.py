"""
Given a string s, return the longest palindromic substring in s.
"""


def longestPalindrome(s):
    def helper(s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return s[j + 1: k]

    result = ""
    for i in range(len(s)):
        subp = helper(s, i, i)
        if len(subp) > len(result):
            result = subp
        subp = helper(s, i, i + 1)
        if len(subp) > len(result):
            result = subp
    return result

if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))
    # bab

    s = "cbbd"
    print(longestPalindrome(s))
    # bb
