'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
    i = 0
    collect = ""
    max_len = 0
    while i < len(s):
        if s[i] in collect:
            collect = collect[collect.find(s[i]) + 1:] + s[i] #Remove till the last occurrence of present char
        else:
            collect += s[i]
        max_len = max(max_len, len(collect))
        i += 1
    return max_len


if __name__ == '__main__':

    s = "aabaab!bb"
    print(lengthOfLongestSubstring(s))
    # Returns 3