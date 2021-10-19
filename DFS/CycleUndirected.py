"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not.
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def dfs(self, v, visited, parent):
        visited[v] = True
        for node in self.graph[v]:
            if not visited[node]:
                if self.dfs(node, visited, v):
                    return True
            elif node != parent:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.dfs(node, visited, -1):
                    return True
        return False

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    print(g.isCyclic())
    # True

    g1 = Graph(3)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    print(g1.isCyclic())
    # False