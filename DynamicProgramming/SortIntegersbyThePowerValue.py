"""
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

    if x is even then x = x / 2
    if x is odd then x = 3 * x + 1

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [lo, hi] sorted by the power value.
"""


def getKth(lo, hi, k):
    def power(num, memo={}):
        if num in memo:
            return memo[num]
        if num == 1:
            return 0
        if num % 2 == 0:
            memo[num] = 1 + power(num / 2, memo)
            return memo[num]
        else:
            memo[num] = 1 + power(3 * num + 1, memo)
            return memo[num]

    d = {num: power(num) for num in range(lo, hi + 1)}
    d = dict(sorted(d.items(), key=lambda x: x[1]))
    print(d)

    return list(d.keys())[k - 1]

if __name__ == '__main__':
    getKth(lo = 7, hi = 15, k = 2)
    # Returns 10
    # d = {8: 3, 10: 6, 12: 9, 13: 9, 11: 14, 7: 16, 14: 17, 15: 17, 9: 19}
