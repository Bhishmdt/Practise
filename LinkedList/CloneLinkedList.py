"""
You are given a Double Link List with one pointer of node pointing to the next node just like in a single link list.
The second pointer however CAN point to any node in the list and not just the previous node. Now write a program in O(n)
 time to duplicate this list. That is, write a program which will create a copy of this list.

Let us call the second pointer as random pointer as it can point to any arbitrary node in the linked list.
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def clone(head):
    curr = head
    while curr:
        dummy = Node(curr.val)
        dummy.next = curr.next
        curr.next = dummy
        curr = curr.next.next

    curr = head
    while curr:
        curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    copy = head.next
    while curr.next:
        temp = curr.next
        curr.next = curr.next.next
        curr = temp

    return copy

def printDLL(root):

    curr = root
    while curr:
        print('Data =', curr.val, ', Random =', curr.random.val)
        curr = curr.next

if __name__ == '__main__':
    '''Create a doubly linked list'''
    original_list = Node(1)
    original_list.next = Node(2)
    original_list.next.next = Node(3)
    original_list.next.next.next = Node(4)
    original_list.next.next.next.next = Node(5)

    '''Set the random pointers'''

    # 1's random points to 3
    original_list.random = original_list.next.next

    # 2's random points to 1
    original_list.next.random = original_list

    # 3's random points to 5
    original_list.next.next.random = original_list.next.next.next.next

    # 4's random points to 5
    original_list.next.next.next.random = original_list.next.next.next.next

    # 5's random points to 2
    original_list.next.next.next.next.random = original_list.next

    '''Print the original linked list'''
    print('Original list:')
    printDLL(original_list)

    '''Create a duplicate linked list'''
    cloned_list = clone(original_list)

    '''Print the duplicate linked list'''
    print('\nCloned list:')
    printDLL(cloned_list)

    """
    Original list:
Data = 1 , Random = 3
Data = 2 , Random = 1
Data = 3 , Random = 5
Data = 4 , Random = 5
Data = 5 , Random = 2

Cloned list:
Data = 1 , Random = 3
Data = 2 , Random = 1
Data = 3 , Random = 5
Data = 4 , Random = 5
Data = 5 , Random = 2
    """
