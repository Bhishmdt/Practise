"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.
"""


def partitionLabels(s):
    last = {}
    for i, c in enumerate(s):
        last[c] = i
    i = 0
    result = []
    while i < len(s):
        start = i
        end = last[s[i]]
        while i < end:
            i += 1
            end = max(end, last[s[i]])
        result.append(end - start + 1)
        i += 1
    return result

if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))
    # Returns [9, 7, 8]

    s = "eccbbbbdec"
    print(partitionLabels(s))
    # Returns [10]