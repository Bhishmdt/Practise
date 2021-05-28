"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    for n, a in prerequisites:
        graph[n].append(a)
    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False
    return True

def dfs(graph, visited, i):
    # if node in being visited state, then cycle is found
    if visited[i] == 2:
        return False
    # check if state of node is visited
    if visited[i] == 1:
        return True
    # mark as being visited
    visited[i] = 2
    # visit all the adjacent nodes
    for a in graph[i]:
        if not dfs(graph, visited, a):
            return False
    visited[i] = 1
    return True

if __name__ == '__main__':
    numCourses = 4

    prerequisites = [[3, 2], [3, 1], [2, 0], [2, 1], [0, 1]]
    print(canFinish(numCourses, prerequisites))
    # Returns True

    prerequisites = [[3, 2], [3, 1], [2, 0], [1, 2], [0, 1]] # 2, 0, 1 cycle
    print(canFinish(numCourses, prerequisites))
    # Returns False