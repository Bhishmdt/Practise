"""
All Paths From Source to Target
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).
"""

def allPathsSourceTarget(graph):
    def dfs(curr, path):
        # If we reach the target node, append
        if curr == len(graph) -1:
            result.append(path)
        else:
            # Move to the next node and append current node to path
            for i in graph[curr]:
                dfs(i, path + [i])
    result = []
    # Start from 0 Node
    dfs(0, [0])
    return result

if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    print(allPathsSourceTarget(graph))
    # Returns [[0, 1, 3], [0, 2, 3]]

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(allPathsSourceTarget(graph))
    # Returns [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]