"""
Given a string S, find length of the longest substring with all distinct characters.
"""

def find_longest(S):
    start = -1
    d = {}
    maxlen = 0
    for i, e in enumerate(S):
        if e in d:
            start = d[e]
            d = {}
        maxlen = max(maxlen, i - start)
        d[e] = i


    return maxlen

if __name__ == '__main__':
    S = "geeksforgeeks"
    print(find_longest(S))
    # 7

    S = "geekgsgfogrgeeks"
    print(find_longest(S))
    # 4

    S = "ehger"
    print(find_longest(S))
    # 4