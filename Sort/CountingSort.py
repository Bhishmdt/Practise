"""
Count sort
"""


def countSort(A):
    output = [0 for _ in range(len(A))]
    count = [0 for _ in range(256)]

    result = [None for _ in A]

    for e in A:
        count[ord(e)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(A)):
        output[count[ord(A[i])] - 1] = A[i]
        count[ord(A[i])] -= 1

    for i in range(len(A)):
        result[i] = output[i]
    return result

if __name__ == '__main__':
    A = "jsjh78278"
    print(countSort(A))
    # Returns ['2', '7', '7', '8', '8', 'h', 'j', 'j', 's']