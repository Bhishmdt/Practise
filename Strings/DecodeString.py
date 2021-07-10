"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
"""


def decodeString(s):
    stack = []
    currnum = 0
    currstr = ''
    for e in s:
        if e.isdigit():
            currnum = currnum * 10 + int(e)
        elif e == '[':
            stack.append(currstr)
            stack.append(currnum)
            currstr = ''
            currnum = 0
        elif e == ']':
            num = stack.pop()
            prevstr = stack.pop()
            currstr = prevstr + num * currstr
        else:
            currstr += e
    return currstr

if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    print(decodeString(s))
    # Returns abcabccdcdcdef

    s = "3[a2[c]]"
    print(decodeString(s))
    # Returns  accaccacc
