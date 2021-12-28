"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""


def insert(intervals, newInterval):
    start, end = newInterval[0], newInterval[1]
    left, right = [], []
    for e in intervals:
        if e[1] < start:
            left.append(e)
        elif e[0] > end:
            right.append(e)
        else:
            start = min(start, e[0])
            end = max(end, e[1])
    return left + [[start, end]] + right

if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))
    # [[1, 2], [3, 10], [12, 16]]