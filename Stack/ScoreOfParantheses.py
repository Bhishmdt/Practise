"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

"""


def scoreOfParentheses(s):
    stack, result = [], 0
    for e in s:
        print(e, stack, result)
        if e == '(':
            stack.append(result)
            result = 0
        else:
            if result:
                result += stack[-1] + result
            else:
                result += stack[-1] + 1
            stack.pop()
    return result

if __name__ == '__main__':
    s = "(())"
    scoreOfParentheses(s)
    print(scoreOfParentheses(s))
    # Returns 2

    s = "(()(()))"
    scoreOfParentheses(s)
    print(scoreOfParentheses(s))
    # Returns 6