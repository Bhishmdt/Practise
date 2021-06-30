"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


def groupAnagrams(strs):
    d = {}
    for e in strs:
        key = tuple(sorted([char for char in e]))
        d[key] = d.get(key, []) + [e]
    return d.values()

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
    # Returns [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]