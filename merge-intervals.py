"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge(intervals):
    result = []
    # Sort the intervals with start index
    intervals = sorted(intervals, key=lambda i: i[0])
    for i in intervals:
        # If start index of current interval is less or equal to previous interval's end index, then merge them.
        # Else append to output
        if result and i[0] <= result[-1][-1]:
            result[-1][-1] = max(result[-1][-1], i[-1])
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # Returns [[1, 6], [8, 10], [15, 18]]

    print(merge([[4, 5], [1, 4]]))
    # Returns  [[1, 5]]