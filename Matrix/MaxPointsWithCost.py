"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

    x for x >= 0.
    -x for x < 0.

"""


# def maxPoints(points):
#     net = 0
#     for i in range(len(points) - 2, -1, -1):
#         for j in range(len(points[0])):
#             max_cell = -float('inf')
#             for k in range(len(points[0])):
#                 max_cell = max(points[i][j] + points[i + 1][k] - abs(j - k), max_cell)
#             points[i][j] = max_cell
#     return max(points[0][:])


def maxPoints(points):
    dp = [0] * len(points[0])
    for line in points:
        for i in range(1, len(line)):
            dp[i] = max(dp[i], dp[i - 1] - 1)
            dp[-i - 1] = max(dp[-i - 1], dp[-i] - 1)
        for i in range(len(line)):
            dp[i] += line[i]
    return max(dp)

if __name__ == '__main__':
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(maxPoints(points))
    # Returns 9