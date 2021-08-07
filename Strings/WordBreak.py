"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s, wordDict):
    res = [True]
    for i in range(1, len(s) + 1):
        temp = False
        for j in range(i):
            temp = temp or res[j] and s[j:i] in wordDict
        res += [temp]
    return res[-1]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))
    # True

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))
    # False