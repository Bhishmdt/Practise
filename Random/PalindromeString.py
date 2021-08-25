"""
Check if a given string is a palindrome string.
"""

def checkPalindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(checkPalindrome("abcba"))
    # True
    print(checkPalindrome("abccba"))
    # True
    print(checkPalindrome("abcbac"))
    # False