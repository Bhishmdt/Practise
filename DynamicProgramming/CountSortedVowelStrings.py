"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
"""


def countVowelStrings(n):
    dp = [0] + [1] * 5
    for i in range(1, n + 1):
        for k in range(1, 6):
            dp[k] += dp[k - 1]
    return dp[5]

if __name__ == '__main__':
    print(countVowelStrings(3))
    # 35
    print(countVowelStrings(4))
    # 70