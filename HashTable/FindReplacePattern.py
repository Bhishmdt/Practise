"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
"""


def findAndReplacePattern(words, pattern):
    def findpattern(word):
        d = {}
        i = 0
        for w in word:
            if w not in d.keys():
                d[w] = i
                i += 1
        return "".join([str(d[e]) for e in word])

    checkPattern = findpattern(pattern)
    result = []
    for word in words:
        if findpattern(word) == checkPattern:
            result.append(word)
    return result

if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(findAndReplacePattern(words, pattern))
    # Returns ['mee', 'aqq']

    words = ["a", "b", "c"]
    pattern = "a"
    print(findAndReplacePattern(words, pattern))
    # Returns ["a", "b", "c"]