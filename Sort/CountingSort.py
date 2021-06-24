"""
Count sort
"""


def countSort(A):
    output = [None for _ in range(len(A))]
    count = [0 for _ in range(256)]

    for e in A:
        count[ord(e)] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in range(len(A)):
        output[count[ord(A[i])] - 1] = A[i]
        count[ord(A[i])] -= 1

    return output

def countSortWithNegative(A):
    max_element = max(A)
    min_element = min(A)
    range_of_elements = max_element - min_element + 1

    output = [0 for _ in range(len(A))]
    count = [0 for _ in range(range_of_elements)]

    for i in range(len(A)):
        count[A[i] - min_element] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(A)):
        output[count[A[i] - min_element] - 1] = A[i]
        count[A[i] - min_element] -= 1
        
    return output

if __name__ == '__main__':
    A = "jsjh78278"
    print(countSort(A))
    # Returns ['2', '7', '7', '8', '8', 'h', 'j', 'j', 's']
    
    B = [-2, -1, -4, -6, 7, 9]
    print(countSortWithNegative(B))
    # Returns [-6, -4, -2, -1, 7, 9]