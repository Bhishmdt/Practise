"""

"""


def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    def helper(beginWord, endWord, wordList, n, result):
        if beginWord == endWord:
            result.append(n)
        if beginWord == "$#@":
            return
        for i in range(len(wordList)):
            if wordList[i] == "$#@":
                continue
            temp = wordList[i]
            if len(set(split(beginWord)) | set(split(wordList[i]))) == (len(wordList[i]) + 1):
                # print(beginWord, n)
                wordList[i] = "$#@"
                helper(temp, endWord, wordList, n + 1, result)
            if temp not in wordList:
                wordList[i] = temp
        return 0

    result = []
    helper(beginWord, endWord, wordList, 1, result)
    if result:
        return min(result)
    else:
        return 0

def split(word):
    return [char for char in word]

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))
    # Returns 5

    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    print(ladderLength(beginWord, endWord, wordList))
    # Returns 2

