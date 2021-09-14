"""
Find index of right smaller element
"""


def findRightSmaller(arr):
    right = [0] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        if not stack:
            right[i] = len(arr) - 1
            stack.append(i)
        elif stack and arr[i] <= arr[stack[-1]]:
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()

            if not stack:
                right[i] = len(arr) - 1
            else:
                right[i] = stack[-1] - 1
            stack.append(i)
        else:
            right[i] = stack[-1] - 1
            stack.append(i)
    return right


if __name__ == '__main__':
    arr = [2, 1, 5, 6, 2, 2]
    print(leftSmaller(arr))