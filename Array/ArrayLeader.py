"""
Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
Let the input array be arr[] and size of the array be size.
"""

def printLeaders(A):
    stack = []
    for e in A:
        while stack and stack[-1] <= e:
            stack.pop()
        stack.append(e)

    return stack

if __name__ == '__main__':
    A = [16, 17, 4, 3, 5, 2]
    print(printLeaders(A))
    # [17, 5, 2]