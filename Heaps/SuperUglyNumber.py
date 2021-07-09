"""
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
"""

import heapq

def nthSuperUglyNumber(n, primes):
    heap = [(p, p, 1) for p in primes]
    heapq.heapify(heap)
    result = [1]
    c = 0
    while c < n - 1:

        currmin, p, i = heapq.heappop(heap)
        if currmin == result[-1]:
            heapq.heappush(heap, (p * result[i], p, i + 1))
            continue
        c += 1
        result.append(currmin)
        heapq.heappush(heap, (p * result[i], p, i + 1))

    return result[-1]

if __name__ == '__main__':
    print(nthSuperUglyNumber(12, [2, 7, 13, 19]))
    # Returns 32

    print(nthSuperUglyNumber(15, [2, 3, 5, 7, 11, 13, 17, 19]))
    # Return 15
