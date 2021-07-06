"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.
"""


def countAndSay(n):
    def helper(s):
        result = ''
        currstr = s[0]
        c = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
            else:
                result += str(c) + currstr
                currstr = s[i]
                c = 1
        result += str(c) + currstr

        return result

    start = '1'
    for i in range(n - 1):
        start = helper(start)
    return start

if __name__ == '__main__':
    for i in range(10):
        print(countAndSay(i))
    """
    Returns 
    1
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    31131211131221
    """
