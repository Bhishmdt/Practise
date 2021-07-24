"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
"""


def removeKdigits(num, k):
    stack = []
    for e in num:
        while k > 0 and len(stack) > 0 and stack[-1] > e:
            k -= 1
            stack.pop()
        stack.append(e)
    if k > 0:
        stack = stack[:-k]
    result = "".join(stack).lstrip("0")
    if result:
        return result
    return "0"

if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(removeKdigits(num, k))
    # Returns 1219

    num = "10200"
    k = 1
    print(removeKdigits(num, k))
    # Returns 200