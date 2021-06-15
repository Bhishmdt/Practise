"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
"""
import heapq

def reorganizeString(S):
    if not S:
        return ""
    d = {}
    for e in S:
        d[e] = d.get(e, 0) + 1
    h = [(-d[k], k) for k in d]
    heapq.heapify(h)

    result = ""
    while len(h) > 1:
        freqa, a = heapq.heappop(h)
        freqb, b = heapq.heappop(h)
        result += a
        result += b

        if freqa < -1:
            heapq.heappush(h, (freqa + 1, a))
        if freqb < -1:
            heapq.heappush(h, (freqb + 1, b))

    if h:
        freq, char = h[0]
        if freq < -1:
            return ""
        else:
            result += char
    return result

if __name__ == '__main__':
    print(reorganizeString("aaabcbccama"))
    # Returns "acabacabacm"
    print(reorganizeString("abaa"))
    # Returns ""
    print(reorganizeString("abccba"))
    # Returns abcabc