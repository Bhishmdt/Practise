"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    sentinalL = ListNode()
    sentinalR = ListNode()
    sentinall = ListNode()
    sentinalr = ListNode()
    sentinall.next = sentinalL
    sentinalr.next = sentinalR
    while head:
        if head.val < x:
            sentinalL.next = head
            head = head.next
            sentinalL = sentinalL.next
        else:
            sentinalR.next = head
            head = head.next
            sentinalR = sentinalR.next
    sentinalR.next = None
    sentinalL.next = sentinalr.next.next

    return sentinall.next.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    printLL(partition(head, 3))
    # Returns 1 2 2 4 3 5




