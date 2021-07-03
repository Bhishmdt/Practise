"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.
"""

import heapq
import math

def minSetSize(arr):
    min_remove = math.ceil(len(arr) // 2)
    d = {}
    for e in arr:
        d[e] = d.get(e, 0) + 1

    h = [(-d[k], k) for k in d]
    heapq.heapify(h)

    result = 0
    while min_remove > 0:
        result += 1
        min_remove -= -heapq.heappop(h)[0]


    return result

if __name__ == '__main__':
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    print(minSetSize(arr))
    # Returns 2

    arr = [1, 9]
    print(minSetSize(arr))
    # Returns 2
