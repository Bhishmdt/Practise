"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee,
manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates,
and they will inform their subordinates, and so on until all employees know about the urgent news.
The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes,
all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news.
"""


def numOfMinutes(n, headID, manager, informTime):
    def dfs(i):
        if manager[i] != -1:
            informTime[i] += dfs(manager[i])
            manager[i] = -1
        return informTime[i]

    result = []
    for i in range(n):
        result.append(dfs(i))
    return max(result)

if __name__ == '__main__':
    n = 6
    headID = 2
    manager = [2, 2, -1, 2, 2, 2]
    informTime = [0, 0, 1, 0, 0, 0]
    print(numOfMinutes(n, headID, manager, informTime))
    # Returns 1

    n = 7
    headID = 6
    manager = [1, 2, 3, 4, 5, 6, -1]
    informTime = [0, 6, 5, 4, 3, 2, 1]
    print(numOfMinutes(n, headID, manager, informTime))
    # Returns 21

    n = 15
    headID = 0
    manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    print(numOfMinutes(n, headID, manager, informTime))
    # Returns 3
