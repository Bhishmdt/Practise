"""
Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLL(head1, head2):
    sentinal, head = ListNode(), ListNode()
    sentinal.next = head
    while head1 and head2:
        if head1.val < head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    if head1:
        head.next = head1
    else:
        head.next = head2

    return sentinal.next.next

def printLL(head):
    while head:
        print(head.val, end="\t")
        head = head.next

    print("\n")

if __name__ == '__main__':
    head1 = ListNode(2)
    head1.next = ListNode(7)
    head1.next.next = ListNode(15)
    head1.next.next.next = ListNode(21)

    head2 = ListNode(2)
    head2.next = ListNode(5)
    head2.next.next = ListNode(17)
    head2.next.next.next = ListNode(30)
    head2.next.next.next.next = ListNode(35)
    
    printLL(mergeLL(head1, head2))
    # 2	2	5	7	15	17	21	30	35