"""
Given a Directed Acyclic Graph having V vertices and E edges, where each edge {U, V} represents the Jobs U and V such
that Job V can only be started only after completion of Job U.
The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        # Dictionary containing adjacency List
        self.graph = defaultdict(list)
        self.n = vertices

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printOrder(self, n):
        # Initialize indegree with 0
        indegree = [0] * (self.n + 1)
        # Calculate indegree for all the nodes
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1
        # Initialize time with zeros
        time = [0] * (self.n + 1)
        queue = []
        # Initialize all nodes of 0 indegree with time as 1 and append to queue
        for i in range(1, self.n + 1):
            if indegree[i] == 0:
                queue.append(i)
                time[i] = 1
        while queue:
            # Visit adjacent nodes in the order of queue
            front_node = queue.pop(0)
            for adj_node in self.graph[front_node]:
                indegree[adj_node] -= 1
                if (indegree[adj_node] == 0):
                    # When the indegree of adjacent node is 0, add 1 to the front_node for time of adjacent node and append to queue.
                    time[adj_node] = time[front_node] + 1
                    queue.append(adj_node)
        for i in range(1, n + 1):
            print(i, " - ", time[i], end="\n")

if __name__ == '__main__':
    n = 10
    g = Graph(n)

    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 6)
    g.addEdge(2, 9)
    g.addEdge(3, 6)
    g.addEdge(3, 7)
    g.addEdge(4, 9)
    g.addEdge(5, 6)
    g.addEdge(5, 8)
    g.addEdge(6, 8)
    g.addEdge(7, 8)
    g.addEdge(8, 10)
    g.addEdge(8, 9)
    g.addEdge(9, 10)

    g.printOrder(n)
    """
    Time taken by each job.
    1  -  1
    2  -  1
    3  -  1
    4  -  2
    5  -  2
    6  -  3
    7  -  2
    8  -  4
    9  -  5
    10  -  6
    """