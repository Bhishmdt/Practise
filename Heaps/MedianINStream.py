"""
Given an input stream of N integers.
The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.
"""
from heapq import *

class MedianStream:
    def __init__(self):
        self.left = []
        self.right = []

    def insertHeap(self, x):
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, x))
        else:
            heappush(self.right, -heappushpop(self.left, -x))

    def getMedian(self):
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        else:
            return -self.left[0]

if __name__ == '__main__':
    obj = MedianStream()
    while True:
        n = input('Enter number or character to exit: ')
        try:
            x = int(n)
            obj.insertHeap(x)
            print(f"Median is: {obj.getMedian()}")
        except ValueError:
            break


