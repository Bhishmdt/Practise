"""
Given a string expression of numbers and operators, return all possible results from computing all the different
possible ways to group numbers and operators. You may return the answer in any order.
"""


def diffWaysToCompute(expression):
    result = []
    for i in range(len(expression)):
        if expression[i] in '+-*':
            for a in diffWaysToCompute(expression[:i]):
                for b in diffWaysToCompute(expression[i + 1:]):
                    if expression[i] == '+':
                        result.append(a + b)
                    elif expression[i] == '-':
                        result.append(a - b)
                    else:
                        result.append(a * b)

    return result or [int(expression)]

if __name__ == '__main__':
    expression = "2*3-4*5"
    print(diffWaysToCompute(expression))
    # Returns [-34, -10, -14, -10, 10]