"""
Find area of largest rectangle in a histogram.
"""
from leftSmaller import findLeftSmaller
from rightSmaller import findRightSmaller

def findMaxArea(arr):
    left = findLeftSmaller(arr)
    right = findRightSmaller(arr)
    max_area = 0
    for i in range(len(arr)):
        max_area = max(max_area, arr[i] * (right[i] - left[i] + 1))
    
    return max_area

if __name__ == '__main__':
    arr = [2, 1, 5, 6, 2, 2]
    print(findMaxArea(arr))