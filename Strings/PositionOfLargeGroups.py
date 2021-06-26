"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group.
In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.
"""


def largeGroupPositions(s):
    result = []
    start = 0
    end = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            end = i
        else:
            if end - start >= 2:
                result.append([start, end])
            start = i
    if end - start >= 2:
        result.append([start, end])
    return result

if __name__ == '__main__':
    s = "abbxxxxzzy"
    print(largeGroupPositions(s))
    # Returns [[3, 6]]

    s = "abcdddeeeeaabbbcd"
    print(largeGroupPositions(s))
    # Returns [[3, 5], [6, 9], [12, 14]]