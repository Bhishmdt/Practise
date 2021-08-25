"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


def isValid(s):
    d = {')': '(', '}': '{', ']': '['}
    stack = []
    for e in s:
        if e in d.values():
            stack.append(e)
        if e in d.keys():
            if stack and stack[-1] == d[e]:
                stack.pop()
            else:
                return False
    return not stack

if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))
    # True

    s = "([)]"
    print(isValid(s))
    # False