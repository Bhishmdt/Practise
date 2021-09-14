"""
Find index of left smaller element
"""

def findLeftSmaller(arr):
    left = [0] * len(arr)
    stack = []
    for i in range(len(arr)):
        if not stack:
            left[i] = 0
            stack.append(i)
        elif stack and arr[i] <= arr[stack[-1]]:
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
                
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        else:
            left[i] = stack[-1] + 1
            stack.append(i)
    return left

if __name__ == '__main__':
    arr = [2, 1, 5, 6, 2, 2]
    print(leftSmaller(arr))