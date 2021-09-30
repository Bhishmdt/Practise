"""
Given a singly linked list of size N. The task is to left-shift the linked list by k nodes,
where k is a given positive integer smaller than or equal to length of the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateLL(head, K):
    if not head:
        return head

    sentinal = ListNode()
    sentinal.next = head
    
    while K > 1:
        head = head.next
        K -= 1
    
    if not head.next:
        return sentinal.next

    temp = head.next
    head.next = None
    head = temp
    
    while head.next:
        head = head.next
    
    head.next = sentinal.next
    
    return temp

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
    printLL(rotateLL(head, 3))
    # 4	5	1	2	3

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    printLL(rotateLL(head, 5))
    # 1	2	3 4 5

