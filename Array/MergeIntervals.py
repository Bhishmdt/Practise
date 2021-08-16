"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge(intervals):
    def takeFirst(elem):
        return elem[0]

    intervals.sort(key=takeFirst)
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i - 1][1] and intervals[i][1] >= intervals[i - 1][1]:
            intervals[i][0] = intervals[i - 1][0]
            intervals.pop(i - 1)
            i -= 1
        elif intervals[i][0] <= intervals[i - 1][1] and intervals[i][1] <= intervals[i - 1][1]:
            intervals[i][0] = intervals[i - 1][0]
            intervals[i][1] = intervals[i - 1][1]
            intervals.pop(i - 1)
            i -= 1
        i += 1
    return intervals

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
    # [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    print(merge(intervals))
    # [[1, 5]]