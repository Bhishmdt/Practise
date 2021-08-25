"""
Given a positive integer array arr of size N, the task is to check if number formed, from any arrangement of array elements, form a palindrome or not.
"""

def checkValidPalindrome(arr):
    d = {}
    for e in arr:
        d[e] = d.get(e, 0) + 1
    
    count = 0
    for e in d:
        if d[e] % 2 != 0:
            count += 1
            
    return not count > 1

if __name__ == '__main__':
    arr = [2, 1, 3, 2, 1]
    print(checkValidPalindrome(arr))
    # True

    arr = [2, 1, 3, 2, 1, 3]
    print(checkValidPalindrome(arr))
    # True

    arr = [2, 1, 3, 2, 1, 3, 3, 1]
    print(checkValidPalindrome(arr))
    # False