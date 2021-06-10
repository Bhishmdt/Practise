"""
Print fibonacci numbers using Tabulation.
"""

def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i < n - 1:
            table[i + 2] += table[i]
    return table[n]

if __name__ == '__main__':
    print(fib(3)) # 2
    print(fib(7)) # 13
    print(fib(8)) # 21
    print(fib(50)) # 12586269025