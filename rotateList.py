"""
Given the head of a linked list, rotate the list to the right by k places.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    l = 0
    sentinal = ListNode()
    sentinal.next = head
    if not head:
        return
    # Point head to last node
    while head.next:
        head = head.next
        l += 1
    l += 1
    r = l - k % l
    curr = sentinal
    # Find (k-l)th Node from end
    while r > 0:
        curr = curr.next
        r -= 1
    # Last node points to first node
    head.next = sentinal.next
    # Next node of curr node is the new head node
    sentinal.next = curr.next
    # Curr node points to None
    curr.next = None
    # Return new head node
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
    printList(rotateRight(head, 2))
    # Returns 4	5	1	2	3
    head = None
    printList(rotateRight(head, 5))
    # Returns