"""
Queue using two Stacks.
"""

class Queue():
    def __init__(self):
        self.Stack1, self.Stack2 = [], []

    def push(self, val):
        self.Stack1.append(val)

    def pop(self):
        self.move()
        return self.Stack2.pop()

    def top(self):
        self.move()
        return self.Stack2[-1]

    def move(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())

if __name__ == '__main__':
    Obj = Queue()
    Obj.push(5)
    Obj.push(2)
    Obj.push(8)
    Obj.push(1)
    print(Obj.pop()) # 5
    print(Obj.top()) # 2