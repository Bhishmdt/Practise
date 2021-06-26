"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

def generateParenthesis(n):
    def generate(p, left, right, result=[]):
        if left:
            generate(p + '(', left - 1, right)
        if right > left:
            generate(p + ')', left, right - 1)
        if right == 0:
            result += [p]
        return result

    return generate("", n, n)

if __name__ == '__main__':
    print(generateParenthesis(3))
    # Returns ['((()))', '(()())', '(())()', '()(())', '()()()']