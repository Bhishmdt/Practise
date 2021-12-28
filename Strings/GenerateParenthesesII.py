"""
Get all valid permutations of l pairs of (), m pairs of [] and n pairs of {}.
"""

def generateParen(l, m, n):
    remaining = [l, l, m, m, n, n]
    brackets = ['(', ')', '[', ']', '{', '}']
    result = []
    num = 2 * (l + m + n)
    def helper(path, remaining, stack):
        if len(path) == num:
            result.append(path)
        for i in range(len(remaining)):
            if i % 2 == 0:
                if remaining[i] > 0:
                    path += brackets[i]
                    stack.append(brackets[i])
                    remaining[i] -= 1
                    helper(path, remaining, stack)
                    remaining[i] += 1
                    path = path[:-1]
                    stack.pop()
            else:
                if stack and stack[-1] == brackets[i - 1]:
                    path += brackets[i]
                    stack.pop()
                    remaining[i] -= 1
                    helper(path, remaining, stack)
                    remaining[i] += 1
                    path = path[:-1]
                    stack.append(brackets[i - 1])
    helper("", remaining, [])
    return result

if __name__ == '__main__':
    print(generateParen(2, 1, 0))
