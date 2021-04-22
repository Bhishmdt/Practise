'''
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters.
If there is more than one possible result, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.
'''

def findLongestWord(s, dictionary):
    #Sort dictionary by length of words in reverse order. If the lengths are equal sort them by lexicographical order
    dictionary.sort(key=lambda x: (-len(x), x))
    for word in dictionary:
        #For each word check if it satisfies the condition
        i = 0
        for c in s:
            #Check if each character in s is present in word
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""

if __name__ == '__main__':
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    print(findLongestWord(s, dictionary))
    #Returns "apple"

    s = "abce"
    dictionary = ["abe", "abc"]
    print(findLongestWord(s, dictionary))
    #Returns "abc"


