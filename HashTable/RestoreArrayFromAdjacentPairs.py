"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]].
The pairs can appear in any order.
Return the original array nums. If there are multiple solutions, return any of them.
"""


def restoreArray(adjacentPairs):
    d = {}
    for e in adjacentPairs:
        d[e[0]] = d.get(e[0], []) + [e[1]]
        d[e[1]] = d.get(e[1], []) + [e[0]]
    result = []
    for k, v in d.items():
        if len(v) == 1:
            result.append(k)
            break
    prev = result[0]
    while len(result) <= len(adjacentPairs):
        for next_item in d.pop(result[-1]):
            if next_item != prev:
                prev = result[-1]
                result += [next_item]
                break
    return result

if __name__ == '__main__':
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    print(restoreArray(adjacentPairs))


