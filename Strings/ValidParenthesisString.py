"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""


def checkValidString(s):
    cmin = cmax = 0
    for i in s:
        if i == '(':
            cmax += 1
            cmin += 1
        if i == ')':
            cmax -= 1
            cmin = max(cmin - 1, 0)
        if i == '*':
            cmax += 1
            cmin = max(cmin - 1, 0)
        if cmax < 0:
            return False
    return cmin == 0

if __name__ == '__main__':
    s = "(*))"
    print(checkValidString(s))
    # Returns True

    s = "((*())"
    print(checkValidString(s))
    # Returns True