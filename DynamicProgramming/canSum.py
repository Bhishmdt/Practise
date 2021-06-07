"""
Check if total of numbers taken from a given array can result in target. Given that all the numbers are positive.
"""

def canSum(target, numbers, memo = None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        if canSum(target - num, numbers, memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False

if __name__ == '__main__':
    print(canSum(7, [2, 3]))
    # Returns True
    print(canSum(7, [2, 4, 3, 7]))
    # Returns True
    print(canSum(9, [2, 4]))
    # Returns False
    print(canSum(300, [7, 14]))
    # Returns False