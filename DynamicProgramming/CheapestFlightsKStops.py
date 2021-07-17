"""
There are n cities connected by some number of flights.
 You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""
import heapq
import collections

def findCheapestPrice(n, flights, src, dst, k):
    heap = [(0, src, k + 1)]
    adj = collections.defaultdict(list)
    for s, t, p in flights:
        adj[s].append((t, p))
    vis = [0] * n
    while heap:
        cost, node, K = heapq.heappop(heap)
        if node == dst:
            return cost
        if vis[node] >= K:
            continue
        vis[node] = K
        for t, p in adj[node]:
            heapq.heappush(heap, (cost + p, t, K - 1))

    return -1

if __name__ == '__main__':
    n = 3
    flights = [[0, 1, 100],
               [1, 2, 100],
               [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(findCheapestPrice(n, flights, src, dst, k))
    # Returns 200

    n = 3
    flights = [[0, 1, 100],
               [1, 2, 100],
               [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(findCheapestPrice(n, flights, src, dst, k))
    # Returns 500