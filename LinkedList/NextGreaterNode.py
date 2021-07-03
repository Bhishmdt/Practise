"""
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    # Go to the last node and check backwards if prev value is greater than current value
    if not head:
        return []
    nums = []
    while head:
        nums.append(head.val)
        head = head.next

    pos = -1
    stack = []
    ans = []

    for i in range(len(nums)):
        pos += 1
        ans.append(0)
        while stack and stack[-1][1] < nums[i]:
            idx, _ = stack.pop()
            ans[idx] = nums[i]

        stack.append((pos, nums[i]))
    return ans

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(7)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next = ListNode(1)
    print(nextLargerNodes(head))
