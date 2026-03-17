def longest_substring(s):
    char=set()
    left=0
    res=0

    for right in range(len(s)):
        while s[right] in char:
            char.remove(s[left])
            left+=1
        char.add(s[right])
        res=max(res,right-left+1)

    return res

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
