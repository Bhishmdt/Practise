"""
Write a function that should return a boolean indicating whether or not the target word can be constructed
by concatenating elements of a given array.
"""

def canConstruct(target, wordbank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in wordbank:
        if target.find(word) == 0:
            if canConstruct(target[len(word):], wordbank, memo):
                memo[target] =True
                return True
    memo[target] = False
    return False

if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    # Returns True

    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    # Returns False

    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
    # Returns False