"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)
    start = ListNode()
    sentinal = ListNode()
    start.next = sentinal
    while heap:
        value, i, head = heapq.heappop(heap)
        if head.next is not None:
            heapq.heappush(heap, (head.next.val, i, head.next))
        sentinal.next = head
        sentinal = sentinal.next

    return start.next.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    printLL(mergeKLists([l1, l2, l3]))
    # Returns 1	 1	2	3	4	4	5	6