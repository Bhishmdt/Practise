"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
"""

def reverseWords(S):
    A = list(S)
    reverseString(A, 0, len(A) - 1)

    l, r = 0, 0
    while r < len(A):
        while r < len(A) and A[r] != '.':
            r += 1
        reverseString(A, l, r - 1)
        r += 1
        l = r
    
    return "".join(A)

def reverseString(A, l, r):
    while l < r:
        A[l], A[r] = A[r], A[l]
        l += 1
        r -= 1
    return A

if __name__ == '__main__':
    S = "i.like.this.program.very.much"
    print(reverseWords(S))
    # "much.very.program.this.like.i"