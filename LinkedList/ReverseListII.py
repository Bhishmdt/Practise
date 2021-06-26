"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if left == right:
        return head
    sentinal = ListNode()
    sentinal.next = head
    prev = sentinal
    for i in range(left - 1):
        prev = prev.next

    pre = None
    cur = prev.next
    print(cur.val)
    for i in range(right - left + 1):
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    prev.next.next = cur
    prev.next = pre

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

    printLL(reverseBetween(head, 2, 4))
    # Returns 1 4 3 2 5