"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

    Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on s.
"""
import re

def maximumGain(s, x, y):
    if x < y:
        smaller, bigger = ('ab', 'ba')
    else:
        smaller, bigger = ('ba', 'ab')

    s_val, b_val = min(x, y), max(x, y)

    result = 0
    s = re.split('[c-z]+', s)

    for char in s:
        count_b, count_s = 1, 1
        while count_s != 0 and count_b != 0:
            count_b = char.count(bigger)
            result += b_val * count_b
            char = char.replace(bigger, '')
            if count_b > 0:
                continue
            count_s = char.count(smaller)
            result += s_val * count_s
            char = char.replace(smaller, '')

    return result

if __name__ == '__main__':
    s = "aabbaaxybbaabb"
    x = 5
    y = 4
    print(maximumGain(s, x, y))
    # Returns 20

    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(maximumGain(s, x, y))
    # Returns 19