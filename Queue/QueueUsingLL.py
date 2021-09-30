"""
Implement a Queue using Linked List.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue():
    def __init__(self):
        self.front, self.end = None, None

    def push(self, val):
        if not self.end:
            self.front = self.end = ListNode(val)
            return
        self.end.next = ListNode(val)
        self.end = self.end.next

    def pop(self):
        if not self.front:
            return
        popped = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return popped

    def top(self):
        return self.front.val

if __name__ == '__main__':
    Obj = Queue()
    Obj.push(5)
    Obj.push(2)
    Obj.push(8)
    Obj.push(1)
    print(Obj.pop()) # 5
    print(Obj.top()) # 2