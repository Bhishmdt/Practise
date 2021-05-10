"""
Find duplicates in an array
"""

def findDuplicates(A):
    result = []
    s = set()
    
    for e in A:
        # If element is already in set, it is a duplicate element.
        if e in s:
            result.append(e)
        else:
            s.add(e)
    return result

if __name__ == '__main__':
    A = [1, 2, 2, 1, 5, 6, 4, 4]
    print(findDuplicates(A))
    # Returns [2, 1, 4]

    A = [1, 2, 3, 4, 5]
    print(findDuplicates(A))
    # Returns []