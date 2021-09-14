"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""


def isMatch(s, p):
    dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(1, len(p) + 1):
        if p[j - 1] != '*':
            break
        dp[0][j] = True

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
    return dp[-1][-1]

if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    print(isMatch(s, p))
    # True

    s = "acdcb"
    p = "a*c?b"
    print(isMatch(s, p))
    # False
