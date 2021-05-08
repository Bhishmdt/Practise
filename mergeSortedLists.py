"""
Merge two sorted linked list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSortedLists(p, q):
    sentinal = ListNode()
    current = ListNode()
    sentinal.next = current
    # add nodes after comparing p and q nodes
    while p and q:
        if p.val < q.val:
            current.next = p
            p = p.next
            current = current.next
        else:
            current.next = q
            q = q.next
            current = current.next
    # add remaining p and q nodes
    while p:
        current.next = p
        p = p.next
        current = current.next
    while q:
        current.next = q
        q = q.next
        current = current.next
    
    return sentinal.next.next

def printList(head):
    while head:
        print(head.val, end="\t")
        head = head.next
    print()


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(5)
    a.next.next = ListNode(9)
    a.next.next.next = ListNode(14)
    a.next.next.next.next = ListNode(20)

    b = ListNode(2)
    b.next = ListNode(3)
    b.next.next = ListNode(5)
    b.next.next.next = ListNode(10)
    b.next.next.next.next = ListNode(16)
    
    printList(mergeSortedLists(a, b))
    # 1	 2	3	5	5	9	10	14	16	20