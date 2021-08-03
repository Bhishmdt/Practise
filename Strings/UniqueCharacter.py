"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def firstUniqChar(s):
    d = {}
    for e in s:
        d[e] = d.get(e, 0) + 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1

if __name__ == '__main__':
    s = "leetcode"
    print(firstUniqChar(s))
    #Returns 0

    s = "loveleetcode"
    print(firstUniqChar(s))
    # Returns 2

    s = "aabb"
    print(firstUniqChar(s))
    # Returns -1