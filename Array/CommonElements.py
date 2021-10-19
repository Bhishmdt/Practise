"""
Given two list v1 and v2. Return the list of elements common to both the lists and return list in sorted order.
"""

def findCommon(V1, V2):
    d = {}
    result = []
    for e in V1:
        d[e] = d.get(e, 0) + 1

    for e in V2:
        if e in d and d[e] > 0:
            result.append(e)
            d[e] -= 1

    return sorted(result)

if __name__ == '__main__':
    V1 = [1, 4, 2, 3, 2, 3, 7]
    V2 = [ 1, 3, 2, 2, 7]
    print(findCommon(V1, V2))
    # [1, 2, 2, 3, 7]