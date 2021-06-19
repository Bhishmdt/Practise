"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
"""

def nthUglyNumber(n):
    start = 1
    while n > 1:
        start += 1
        if isUglyNumber(start):
            n -= 1

    return start

def isUglyNumber(N, memo = None):
    if memo is None:
        memo = {}
    if N in memo:
        return memo[N]
    if N == 1:
        return True
    check = []
    for e in [2, 3, 5]:
        if N % e == 0:
            check.append(isUglyNumber(N / e, memo))
    if any(check):
        memo[N] = True
        return True
    else:
        memo[N] = False
        return False
    
if __name__ == '__main__':
    print(nthUglyNumber(10))
    # Returns 12
    print(nthUglyNumber(200))
    # Returns 16200