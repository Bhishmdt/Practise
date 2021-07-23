"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s
and removing them, causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""


def removeDuplicates(s, k):
    stack = [['$', 1]]
    for char in s:
        if stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    result = ""
    for char, k in stack:
        result += char * k
    return result[1:]

if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(removeDuplicates(s, k))
    # Returns 'aa'

    s = "pbbcggttciiippooaais"
    k = 2
    print(removeDuplicates(s, k))
    # Returns 'ps'
