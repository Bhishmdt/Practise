"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
"""


def canVisitAllRooms(rooms):
    visited = set()
    visited.add(0)

    def dfs(i):
        for j in rooms[i]:
            if j not in visited:
                visited.add(j)
                dfs(j)

    dfs(0)
    return len(visited) == len(rooms)

if __name__ == '__main__':
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(canVisitAllRooms(rooms))
    # Returns False

    rooms = [[1], [2], [3], []]
    print(canVisitAllRooms(rooms))
    # Returns True
