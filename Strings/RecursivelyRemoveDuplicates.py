"""
Given a string S, remove all its adjacent duplicate characters recursively.
"""


def removeDuplicates(S):
    stack = []
    count = 0
    for e in S:
        if stack and stack[-1] == e:
            count += 1
        else:
            if count > 0:
                stack.pop()
                count = 0
                if stack and stack[-1] == e:
                    count += 1
                else:
                    stack.append(e)
            else:
                stack.append(e)
    if count > 0:
        stack.pop()
    return "".join(stack)

if __name__ == '__main__':
    S = "geeksforgeeks"
    print(removeDuplicates(S))
    # gksforgks

    S = "acaaabbbacddd"
    print(removeDuplicates(S))
    # acac

    S = "acabbbaccddd"
    print(removeDuplicates(S))
    # a

