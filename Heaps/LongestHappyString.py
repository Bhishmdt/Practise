"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:

    s is happy and longest possible.
    s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
    s will only contain 'a', 'b' and 'c' letters.

If there is no such string s return the empty string "".
"""
import heapq

def longestDiverseString(a , b, c):
    # Create max-heap
    heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
    heapq.heapify(heap)
    result = ""

    while len(heap) > 0:
        num, char = heapq.heappop(heap)
        # If previous 2 characters are equal to char, add the next character
        if len(result) >= 2 and result[-1] == char and result[-2] == char:
            if len(heap) > 0:
                next_num, next_char = heapq.heappop(heap)
                if next_num == 0:
                    continue
                result += next_char
                next_num += 1
                if next_num != 0:
                    heapq.heappush(heap, (next_num, next_char))
                heapq.heappush(heap, (num, char))
            continue

        if num == 0:
            continue
        result += char
        num += 1
        if num != 0:
            heapq.heappush(heap, (num, char))
    return result

if __name__ == '__main__':
    a = 1
    b = 1
    c = 7
    print(longestDiverseString(a, b, c))
    # Returns ccaccbc

    a = 7
    b = 1
    c = 0
    print(longestDiverseString(a, b, c))
    # Returns aabaa