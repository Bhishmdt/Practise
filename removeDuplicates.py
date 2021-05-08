"""
Remove duplicates from a list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeDuplicates(head):
    s = set()
    s.add(head.val)
    current = head
    # If next node's value is in the set, skip the next value
    while current.next is not None:
        if current.next.val in s:
            current.next = current.next.next
        else:
            s.add(current.next.val)
            current = current.next
            
    return head

def printList(head):
    while head:
        print(head.val, end= "\t")
        head = head.next
    print()
    
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(2)
    printList(removeDuplicates(head))
    # Return 1 2 4

