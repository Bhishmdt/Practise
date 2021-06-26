"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
"""
def removeDuplicateLetters(s):
    if s == "":
        return s
    result = ["!"]
    # Find the last occurrence for each char
    d = {c : i for i, c in enumerate(s)}
    # Visited set
    t = set()
    for i in range(len(s)):
        if s[i] in t:
            continue
        # If last char of result is less than present char and last char of result can be found later, delete the last char
        while s[i] < result[-1] and d[result[-1]] > i:
            t.remove(result.pop())
        result.append(s[i])
        t.add(s[i])
    return "".join(result[1:])

if __name__ == '__main__':
    s = "bcabc"
    print(removeDuplicateLetters(s))
    # Prints "abc"

    s = "cbacdcbc"
    print(removeDuplicateLetters(s))
    # Prints "acdb"

