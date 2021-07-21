"""
You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively.
 Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score.
 The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a, b, and c, return the maximum score you can get.
"""
import heapq

def maximumScore(a, b, c):
    heap = [-a, -b, -c]
    heapq.heapify(heap)
    result = 0

    while len(heap) > 1:
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        if s1 + 1 < 0:
            heapq.heappush(heap, s1 + 1)
        if s2 + 1 < 0:
            heapq.heappush(heap, s2 + 1)
        result += 1
    return result

if __name__ == '__main__':
    a, b, c = 2, 4, 6
    print(maximumScore(a, b, c))
    # Returns 6

    a, b, c = 4, 4, 6
    print(maximumScore(a, b, c))
    # Returns 7