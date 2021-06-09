"""
Write a function that should return number of ways the target word can be constructed
by concatenating elements of a given array.
"""

def canConstruct(target, wordbank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    total = 0

    for word in wordbank:
        if target.find(word) == 0:
            number_of_ways = canConstruct(target[len(word):], wordbank, memo)
            total += number_of_ways
    memo[target] = total
    return total

if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    # Returns 1

    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    # Returns 0

    print(canConstruct("eeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
    # Returns 125