"""
Given a linked list of N nodes such that it may contain a loop.
Remove the loop from the linked list, if it is present.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeCycle(head):
    if not head or not head.next:
        return head

    slow, fast, sentinal = head, head, ListNode()
    sentinal.next = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None
    
    return sentinal.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

    print("\n")

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next
    printLL(removeCycle(head))
    # 1	2	3	4	5	6

