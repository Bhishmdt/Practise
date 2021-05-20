"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(root, k):
    result = []
    sentinal = ListNode()
    sentinal.next = root
    l = 0
    # Find length of Linkedlist
    while root:
        l += 1
        root = root.next
    split = l // k
    rem = l % k
    # Find length of splits
    lengths = [split + 1] * rem + [split] * (k - rem)
    root = sentinal.next
    i, j = 1, 0
    while root:
        if i == lengths[j]:
            result.append(sentinal.next)
            sentinal.next = root.next
            root.next = None
            root = sentinal.next
            # Find cumulative value of lengths, which is used for splitting
            if j < len(lengths) - 1:
                lengths[j + 1] += lengths[j]
                j += 1
        else:
            root = root.next
        i += 1
    # Append any not appended split
    if sentinal.next:
        result.append(sentinal.next)
    # Append None for rest
    i = len(result)
    while i < k:
        result.append(None)
        i += 1
    return result

def ListofLinkedList(A):
    result = []
    for root in A:
        if not root:
            result.append(None)
        else:
            sublist = []
            while root:
                sublist.append(root.val)
                root = root.next
            result.append(sublist)
    return result

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    print(ListofLinkedList(splitListToParts(root, 5)))
    # Returns [[1], [2], [3], None, None]

    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(6)
    root.next.next.next.next.next.next = ListNode(7)
    root.next.next.next.next.next.next.next = ListNode(8)
    root.next.next.next.next.next.next.next.next = ListNode(9)
    root.next.next.next.next.next.next.next.next.next = ListNode(10)
    print(ListofLinkedList(splitListToParts(root, 3)))
    # Returns [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]