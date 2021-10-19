"""
Given a directed graph, check whether the graph contains a cycle or not.
Your function should return true if the given graph contains at least one cycle, else return false.
"""

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for node in self.graph[v]:
            if not visited[node]:
                if self.dfs(node, visited, recStack):
                    return True
            elif recStack[node]:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if not visited[node]:
                if self.dfs(node, visited, recStack):
                    return True
        return False

if __name__ == '__main__':

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.isCyclic())
    # True