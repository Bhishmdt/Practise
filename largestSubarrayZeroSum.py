"""
Given an array of integers, find the length of longest sub-array with sum equals to zero.
"""

def longestSubarrayZeroSum(A):
    cumsum = 0
    d = {0:-1}
    i, max_len = 0, 0
    while i < len(A):
        cumsum += A[i]
        # If cumulative sum(i) is same as previously encountered cumulative sum(j), the subarray(A[i,j]) sum is zero.
        d[cumsum] = d.get(cumsum, i)
        max_len = max(max_len, i - d[cumsum])
        i += 1
    return max_len

if __name__ == '__main__':
    A = [0, 1, -1, 2, 3, 4, -9]
    print(longestSubarrayZeroSum(A))
    # Returns 7

    A = [0, 1, 2, 3]
    print(longestSubarrayZeroSum(A))
    # Returns 1

    A = [1, 2, 3, -3, 4]
    print(longestSubarrayZeroSum(A))
    # Returns 2