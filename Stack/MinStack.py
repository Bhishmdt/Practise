"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        currmin = self.getMin()
        if currmin == None or val < currmin:
            currmin = val

        self.stack.append((val, currmin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) - 1][1]
        else:
            return None

if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    obj.push(3)
    obj.push(1)
    obj.push(5)
    print(obj.stack) # [(2, 2), (3, 2), (1, 1), (5, 1)]
    obj.pop()
    print(obj.stack) # [(2, 2), (3, 2), (1, 1)]
    print(obj.top()) # 1
    print(obj.getMin()) # 1