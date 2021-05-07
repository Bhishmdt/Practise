"""
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node
from the end (the list is 1-indexed).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    sentinal = ListNode()
    sentinal.next = head
    pre_end,  pre_start = sentinal, sentinal
    end, fast, start = head, head, head
    i = 1
    # Find kth node from start, move fast pointer to kth node
    while i < k:
        pre_start = start
        start = start.next
        fast = fast.next
        i += 1
    # Find the kth node from end
    while fast.next is not None:
        pre_end = end
        end = end.next
        fast = fast.next

    # If both the start and end node are same, no swap needed
    if start == end:
        return head

    # previous nodes points to swapped nodes
    pre_start.next, pre_end.next = end, start
    # swap the next pointers for start and end nodes.
    start.next, end.next = end.next, start.next

    return sentinal.next

def printList(head):
    while head:
        print(head.val, end= "\t")
        head = head.next
    print()

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    printList(swapNodes(head, k))
    # Returns 1 4   3	2	5

    head = ListNode(1)
    k = 1
    printList(swapNodes(head, k))
    # Returns 1

    head = ListNode(1)
    head.next = ListNode(2)
    k = 1
    printList(swapNodes(head, k))
    # Returns 2 1

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 2
    printList(swapNodes(head, k))
    # Returns 1	2	3

