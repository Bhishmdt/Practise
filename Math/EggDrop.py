"""
You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.
You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break,
and any egg dropped at or below floor f will not break.
In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n).
If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the minimum number of moves that you need to determine with certainty what the value of f is.
"""
import math

def twoEggDrop(n):
    # solve x(x+1)/2 = n
    x = (-1 + (1 + 8 * n) ** 0.5) / 2.0

    return math.ceil(x)

if __name__ == '__main__':
    n = 2
    print(twoEggDrop(n))
    # Returns 2

    n = 100
    print(twoEggDrop(n))
    # Returns 14