"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

def longestPalindrome(s):
    d = {}
    # Count each string
    for e in s:
        d[e] = d.get(e, 0) + 1
    odd = False
    length = 0
    for e, count in d.items():
        # Add only even counts
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd = True
    # If any of the counts is odd, add one to length
    if odd:
        return length + 1
    else:
        return length
