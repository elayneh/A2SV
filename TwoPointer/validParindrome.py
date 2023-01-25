#!/usr/bin/python3

def palindrome(s: str) -> bool:
    if len(s) == 0:
        return True
    s = s.lower()
    str1 = ""
    for i in range(len(s)):
        if (s[i].isalnum()):
            str1 += s[i]
    left = 0
    right = len(str1) - 1
    print(str1)
    while left <= right:
        if str1[left] != str1[right]:
            return False
        left += 1
        right -= 1
    return True
