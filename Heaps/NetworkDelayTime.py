"""
You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""
import collections
import heapq

def networkDelayTime(times, n, k):
    heap = [(0, k)]
    d = {}
    adj = collections.defaultdict(list)
    for u, v, t in times:
        adj[u] = adj.get(u, []) + [(v, t)]
    while heap:
        time, node = heapq.heappop(heap)
        if node not in d:
            d[node] = time
            for (v, t) in adj[node]:
                heapq.heappush(heap, (time + t, v))
    if len(d) == n:
        return max(d.values())
    else:
        return -1

if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(networkDelayTime(times, n, k))
    # Returns 2