"""
Python program for Dijkstra's single source shortest path algorithm. The program is for adjacency matrix representation of the graph.
"""

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        col1 = "Vertex"
        col2 = "Distance from source"
        print('{:<30}{:<30}'.format(col1, col2))
        for node in range(self.V):
            print('{:<30}{:<30}'.format(node, dist[node]))

    def minDistance(self, dist, included):
        min = float("inf")
        for i in range(self.V):
            if dist[i] < min and included[i] == False:
                min = dist[i]
                min_index = i
        return min_index

    def dijkstra(self, startnode):
        dist = [float("inf")] * self.V
        dist[startnode] = 0
        included = [False] * self.V

        for _ in range(self.V):
            curr = self.minDistance(dist, included)
            included[curr] = True
            for i in range(self.V):
                if self.graph[curr][i] > 0 and included[i] == False and dist[i] > dist[curr] + self.graph[curr][i]:
                    dist[i] = dist[curr] + self.graph[curr][i]

        self.printSolution(dist)

if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    g.dijkstra(0)
    """
    Vertex                        Distance from source          
    0                             0                             
    1                             4                             
    2                             12                            
    3                             19                            
    4                             21                            
    5                             11                            
    6                             9                             
    7                             8                             
    8                             14      
    """