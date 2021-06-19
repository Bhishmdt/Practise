"""
We are given head, the head node of a linked list containing unique integer values.
We are also given the list nums, a subset of the values in the linked list.
Return the number of connected components in nums, where two values are connected if they appear consecutively in the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head, nums):
    result = 0
    connector = False
    while head:
        if head.val in nums:
            if not head.next:
                result += 1
            # start connection if node in nums
            connector = True
        else:
            # end connection and increase number of components by 1
            if connector == True:
                result += 1
            connector = False
        head = head.next
    return result

if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    nums = [0, 4, 1, 3]

    print(numComponents(head, nums))
    # Returns True