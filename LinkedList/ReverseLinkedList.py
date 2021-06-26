"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None

    while head:
        curr = head.next
        head.next = prev
        prev = head
        head = curr
    return prev

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    
    printLL(reverseList(head))
    # Returns 4 3 2 1
