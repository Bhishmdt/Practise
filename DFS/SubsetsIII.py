"""
Given a set of characters represented by a String, return a list containing all subsets of the characters.
"""

def subsets(s):
    result = []
    s = [e for e in s]
    s.sort()
    if not s:
        return []
    def dfs(s, path):
        result.append(path)
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            dfs(s[i + 1:], path + s[i])
    dfs(s, "")
    return result

if __name__ == '__main__':
    s = "bab"
    print(subsets(s))
    