"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapify(heap)
    start = ListNode()
    sentinal = ListNode()
    start.next = sentinal
    while heap:
        value, i, head = heappop(heap)
        if head.next is not None:
            heappush(heap, (head.next.val, i, head.next))
        sentinal.next = head
        sentinal = sentinal.next

    return start.next.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

if __name__ == '__main__':
    L1 = ListNode(1)
    L1.next = ListNode(5)
    L1.next.next = ListNode(20)
    L1.next.next.next = ListNode(30)

    L2 = ListNode(-1)
    L2.next = ListNode(10)
    L2.next.next = ListNode(21)
    L2.next.next.next = ListNode(34)
    L2.next.next.next.next = ListNode(51)

    L3 = ListNode(3)
    L3.next = ListNode(4)
    L3.next.next = ListNode(5)
    L3.next.next.next = ListNode(7)

    L4 = ListNode(8)
    L4.next = ListNode(10)
    L4.next.next = ListNode(24)
    
    printLL(mergeKLists([L1, L2, L3, L4]))

    # -1	1	3	4	5	5	7	8	10	10	20	21	24	30	34	51	
    
    
    