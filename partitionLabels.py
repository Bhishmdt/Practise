""""
A string S of lowercase English letters is given. We want to partition this string into as many parts as
possible so that each letter appears in at most one part, and return a list of integers representing the
size of these parts.
"""
def partition_labels(S):

    d = {}
    i, l, r = 0, 0, 0
    # We find the last occurrence for each of the letters
    while i < len(S):
        d[S[i]] = i
        i += 1

    result = []
    i = 0
    for e in S:
        # Maximum of the last occurrence of each of the letters in the split is our pointer to split
        r = max(r, d[e])
        if i == r:
            # Store the length of the current split
            result += [r - l + 1]
            # Move the left pointer to start of the next split
            l = i + 1
        i += 1
    return result

if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    print(partition_labels(S))
    # Returns [9, 7, 8]
    # (ababcbaca, defegde, hijhklij)

    S = "abcdafhgfggplkpmnq"
    print(partition_labels(S))
    # Returns [5, 6, 4, 1, 1, 1]
    # (abcda, fhgfgg, plkp, m, n, q)