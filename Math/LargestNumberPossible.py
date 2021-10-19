"""
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.
"""

def find_largest(N, S):
    if S == 0:
        if N == 0:
            return 0
        else:
            return -1
    if S > 9 * N:
        return -1

    result = 0
    for _ in range(N):
        if S >= 9:
            result = result * 10 + 9
            S -= 9

        else:
            result = result * 10 + S
            S = 0
    return result

if __name__ == '__main__':
    print(find_largest(2, 9))
    # 90

    print(find_largest(3, 20))
    # 992
