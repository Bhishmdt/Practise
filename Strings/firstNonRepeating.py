"""
Given an input stream of A of n characters consisting only of lower case alphabets.
The task is to find the first non repeating character, each time a character is inserted to the stream.
If there is no such character then append '#' to the answer.
"""
from collections import deque

def findFirstNonRepeating(s):
    dict = {}
    deq = deque()
    result = []
    for char in s:
        dict[char] = dict.get(char, 0) + 1
        if dict[char] == 1:
            deq.append(char)
        while deq and dict.get(deq[0]) > 1:
            deq.popleft()

        if deq:
            result.append(deq[0])
        else:
            result.append('#')

    return result

if __name__ == '__main__':
    s = "abacgacggb"
    print(findFirstNonRepeating(s))
    # ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', '#']



