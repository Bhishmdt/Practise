"""
Remove Zero Sum Consecutive Nodes from Linked List
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until
there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    sentinal = ListNode()
    sentinal.next = head
    cumsum = 0
    d = {0:sentinal}

    # Store dictionary with cumulative sum as key and last Node with that cumulative sum as value
    while head:
        cumsum += head.val
        d[cumsum] = head
        head = head.next

    cumsum = 0
    head = sentinal
    # If the cumulative sum of present Node is equal to any other node's cumulative sum, then switch the pointer of
    # current node to pointer of last node with the cumsum.
    while head:
        cumsum += head.val
        head.next = d[cumsum].next
        head = head.next

    return sentinal.next

def printList(head):
    while head:
        print(head.val, end= "\t")
        head = head.next
    print()

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(-3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)
    printList(removeZeroSumSublists(head))
    # Returns 3 1

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-3)
    head.next.next.next.next = ListNode(4)
    printList(removeZeroSumSublists(head))
    # Returns 1 2 4

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-3)
    head.next.next.next.next = ListNode(-2)
    printList(removeZeroSumSublists(head))
    # Returns 1