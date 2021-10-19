"""
Find Kth largest number in a stream.
"""
from heapq import *

class KthLargest:
    def __init__(self, K):
        self.heap = []
        self.K = K

    def add(self, val):
        if len(self.heap) <= self.K:
            heappush(self.heap, val)
            if len(self.heap) == self.K:
                heappush(self.heap, val)
                print("Kth largest element is: ", self.heap[0])
            return
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        print("Kth largest element is: ", self.heap[0])

if __name__ == '__main__':
    obj = KthLargest(3)
    while True:
        n = input('Enter number or character to exit: ')
        try:
            x = int(n)
            obj.add(x)
        except ValueError:
            break
