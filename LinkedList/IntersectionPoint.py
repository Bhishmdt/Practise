"""
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(a, b):
    if not a or not b:
        return -1
    A = a
    B = b
    while A is not B:
        if A is None:
            A = b
        else:
            A = A.next
        if B is None:
            B = a
        else:
            B = B.next
    if A:
        return A
    else:
        return -1

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)

    b = ListNode(9)
    b.next = ListNode(10)

    common = ListNode(6)
    common.next = ListNode(7)
    common.next.next = ListNode(8)

    a.next.next.next.next.next = common
    b.next.next = common

    print(getIntersectionNode(a, b).val)
    # 6

