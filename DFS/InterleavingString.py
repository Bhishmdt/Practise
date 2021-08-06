"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
"""


def isInterleave(s1, s2, s3):
    r, c, l = len(s1), len(s2), len(s3)
    if r + c != l:
        return False
    queue, visited = [(0, 0)], set((0, 0))
    while queue:
        x, y = queue.pop(0)
        if x + y == l:
            return True
        if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
            queue.append((x + 1, y));
            visited.add((x + 1, y))
        if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
            queue.append((x, y + 1));
            visited.add((x, y + 1))
    return False

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(isInterleave(s1, s2, s3))
    # Returns False

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1, s2, s3))
    # Returns True
