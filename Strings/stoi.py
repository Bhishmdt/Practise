"""
Your task is to implement the atoi function. The function takes a string as argument and converts it to an integer.
"""

def atoi(S):
    if len(S) == 0:
        return 0
    integer, i = 0, 0
    while i < len(S):
        if S[i].isdigit():
            integer = integer * 10 + ord(S[i]) - ord('0')
        else:
            return -1
        i += 1
    return integer

if __name__ == '__main__':
    S = '123'
    print(atoi(S))
    # 123

    S = "12a"
    print(atoi(S))
    # -1

    S = "0012"
    print(atoi(S))
    # 12