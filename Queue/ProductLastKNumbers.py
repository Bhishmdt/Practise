"""
Implement the class ProductOfNumbers that supports two methods:

1. add(int num)

    Adds the number num to the back of the current list of numbers.

2. getProduct(int k)

    Returns the product of the last k numbers in the current list.
    You can assume that always the current list has at least k numbers.

At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
"""

class ProductOfNumbers:

    def __init__(self):
        self.q = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.q = [1]
        else:
            self.q.append(self.q[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.q) <= k:
            return 0
        return int(self.q[-1] / self.q[-1 - k])

if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2)) # 20
    print(obj.getProduct(3)) # 40
    print(obj.getProduct(4)) # 0
    obj.add(8)
    print(obj.getProduct(2)) # 32
