"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head:
        return []
    sentinal = ListNode()
    sentinal.next = head
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    slow.next = None

    first, second = head, prev
    while second:
        temp = first.next
        first.next = second
        first = second
        second = temp

    return sentinal.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    printLL(reorderList(head))
    # Prints 1 5 2 4 3

