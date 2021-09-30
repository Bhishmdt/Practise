"""
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLLGroups(head, k):
    if not head or not head.next or k <= 1:
        return head
    sentinal = ListNode(0)
    sentinal.next = head
    dummy = sentinal
    start, end = head, head

    while end:
        count = 0
        while end and count < k:
            end = end.next
            count += 1
        if count == k:
            curr, prev = end, start
            for _ in range(k):
                temp = prev.next
                prev.next = curr
                curr = prev
                prev = temp
            dummy.next = curr
            dummy = start
            start = end
        else:
            curr, prev = end, start
            for _ in range(count):
                temp = prev.next
                prev.next = curr
                curr = prev
                prev = temp
            dummy.next = curr
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
    head.next.next.next.next.next.next = ListNode(7)
    printLL(reverseLLGroups(head, 3))
    # 3	 2	1	6	5	4	7

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    printLL(reverseLLGroups(head, 2))
    # 2	 1	4	3	6	5	7