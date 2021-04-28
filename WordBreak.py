"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s, wordDict):
    res = [True]
    for i in range(1, len(s) + 1):
        temp = False
        for j in range(i):
            # Check if s[:i] can be formed by splitting into s[:j] and s[j:i]
            temp = temp or res[j] and s[j:i] in wordDict
        # If temp is true for any of the split, append temp to result
        res += [temp]
    # Check if the last res is True
    return res[-1]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))
    # Returns True

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))
    # Returns True

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))
    # Returns False