"""
Print fibonacci numbers using dynamic programming.
"""

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    print(fib(6), "    ", fib(7), "    ", fib(50))
    # Returns
    # 8      13      12586269025