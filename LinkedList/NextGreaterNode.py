"""
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
"""


def nextLargerNodes(head):
    # Go to the last node and check backwards if prev value is greater than current value
    if not head:
        return []
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    currmax = [nums[-1]]
    last_num = nums[-1]
    nums[-1] = 0
    if len(nums) == 1:
        return nums
    for i in range(len(nums) - 2, -1, -1):
        temp = nums[i]
        if nums[i] > last_num:
            currmax.append(nums[i])
        for j in range(len(currmax) - 1, -1, -1):
            if nums[i] < currmax[j]:
                nums[i] = currmax[j]
                continue
        if nums[i] > currmax[0]:
            currmax = [nums[i]]
            nums[i] = 0
        last_num = temp

    return nums

def abc(nums):
    currmax = [nums[-1]]
    last_num = nums[-1]
    nums[-1] = 0
    if len(nums) == 1:
        return nums
    for i in range(len(nums) - 2, -1, -1):
        temp = nums[i]
        if nums[i] > last_num:
            currmax.append(nums[i])
        for j in range(len(currmax) - 1, -1, -1):
            print(i, nums[i], j, currmax)
            if nums[i] < currmax[j]:
                nums[i] = currmax[j]
                break
        if nums[i] > currmax[0]:
            currmax = [nums[i]]
            nums[i] = 0
        last_num = temp
    print(nums)

if __name__ == '__main__':
    nums = [1, 7, 5, 1, 9, 2, 5, 1]
    abc(nums)
