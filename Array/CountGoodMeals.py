"""
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the ith item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.
"""


def countPairs(deliciousness):
    d = {}
    total = 0
    for e in deliciousness:
        for i in range(22):
            total += d.get(2 ** i - e, 0)
        d[e] = d.get(e, 0) + 1
    return total % 1_000_000_007

if __name__ == '__main__':
    deliciousness = [1, 1, 1, 3, 3, 3, 7]
    print(countPairs(deliciousness))
    # Returns 15