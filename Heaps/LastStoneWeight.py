"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""
import heapq

def lastStoneWeight(A):
    I = [-e for e in A]
    heapq.heapify(I)
    while len(I) > 1 and I[0] != 0:
        heapq.heappush(I, heapq.heappop(I) - heapq.heappop(I))
    return -I[0]

if __name__ == '__main__':
    print(lastStoneWeight([2,7,4,1,8,1]))
    # Returns 1
    print(lastStoneWeight([8,4,2]))
    # Rteurns 2