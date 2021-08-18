"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
"""


def nextGreaterElement(n):
    digits = list(str(n))
    i = len(digits) - 1
    while i > 0 and digits[i] <= digits[i - 1]:
        i -= 1

    if i == 0:
        return -1

    j = i
    while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
        j += 1

    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = digits[i:][::-1]
    ret = int(''.join(digits))

    return ret if ret <= (2 ** 31) - 1 else -1

if __name__ == '__main__':
    n = 123576421
    print(nextGreaterElement(n))
    # 123612457