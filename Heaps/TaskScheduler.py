"""

"""
import heapq
import collections

def leastInterval(tasks, n) :
    if n == 0:
        return len(tasks)
    d = {}
    for e in tasks:
        d[e] = d.get(e, 0) + 1

    heap = [(-d[k], k) for k in d]
    stack = []
    heapq.heapify(heap)
    result = []
    d = collections.defaultdict(int)

    while heap:
        num, char = heapq.heappop(heap)
        if len(result) <= n:
            result.append(char)
            num += 1
            if num < 0:
                stack.append((num, char))
            d[result[-1]] = len(result) - 1
            if not heap and len(result) <= n:
                result.append(":")
                while stack:
                    num, char = stack.pop()
                    heapq.heappush(heap, (num, char))
            if len(result) == n + 1:
                while stack:
                    num, char = stack.pop()
                    heapq.heappush(heap, (num, char))
            continue

        while len(result) - d[char] <= n and heap:
            stack.append((num, char))
            num, char = heapq.heappop(heap)

        if len(result) - d[char] > n:
            result.append(char)
            num += 1
            if num < 0:
                heapq.heappush(heap, (num, char))
        else:
            heapq.heappush(heap, (num, char))
            result.append("")
        while stack:
            num, char = stack.pop()
            heapq.heappush(heap, (num, char))
        d[result[-1]] = len(result) - 1
    return len(result)

if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(leastInterval(tasks, n))
    # Returns 16

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval(tasks, n))
    # Returns 8