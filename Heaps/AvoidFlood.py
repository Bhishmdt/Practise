"""
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

    rains[i] > 0 means there will be rains over the rains[i] lake.
    rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.

Return an array ans where:

    ans.length == rains.length
    ans[i] == -1 if rains[i] > 0.
    ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.

If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
"""
import heapq
import collections

def avoidFlood(rains):
    result = [-1] * len(rains)
    stack = []
    d = collections.defaultdict(list)
    for i, lake in enumerate(rains):
        d[lake].append(i)

    for i in range(len(rains)):
        if rains[i] == 0:
            if stack:
                result[i] = rains[heapq.heappop(stack)]
                d[result[i]].pop(0)
            else:
                result[i] = 1
        else:
            if d[rains[i]] and d[rains[i]][0] < i:
                return []
            if d[rains[i]] and len(d[rains[i]]) > 1:
                heapq.heappush(stack, d[rains[i]][1])
    return result

if __name__ == '__main__':
    rains = [1, 2, 3, 4]
    print(avoidFlood(rains))
    # Result [-1, -1, -1, -1]

    rains = [1, 2, 0, 0, 2, 1]
    print(avoidFlood(rains))
    # Result [-1, -1, 2, 1, -1, -1]

    rains = [1, 2, 0, 1, 2]
    print(avoidFlood(rains))
    # Result []

    rains = [69, 0, 0, 0, 69]
    print(avoidFlood(rains))
    # Result [-1, 69, 1, 1, -1]
