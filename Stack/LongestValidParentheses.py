"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""


def longestValidParentheses(s):
    stack = [0]
    longest = 0
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                longest = max(longest, stack[-1])
            else:
                stack = [0]

    return longest

if __name__ == '__main__':
    s = ')()())('
    print(longestValidParentheses(s))
    # 4
    
    s = ')))((('
    print(longestValidParentheses(s))
    # 0