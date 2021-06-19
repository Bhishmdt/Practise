
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head:
        return head
    odd = head
    even = head.next
    # save start of even nodes
    evenstart = head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    # connect odd node to start of even node
    odd.next = evenstart
    return head

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

    printLL(oddEvenList(head))
    # Returns 1    3	5	2	4
