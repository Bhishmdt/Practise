'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].
'''

def decodeString(s):
    A, string, num = [], '', 0
    for ch in s:
        # Append string and number before bracket
        if ch == '[':
            A.append([string, num])
            string = ''
            num = 0
        # While closing bracket multiply number with present string and add to previous string
        elif ch == ']':
            temp, temp_num = A.pop()
            print(temp, temp_num, string)
            string = temp + temp_num * string
        # Collect number strings and convert to number
        elif ch.isdigit():
            num = num * 10 + int(ch)
        else:
            string += ch
    return string

if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(decodeString(s))
    # Returns 'aaabcbc'

    s = "3[a2[c]]"
    print(decodeString(s))
    # Returns 'accaccacc'

