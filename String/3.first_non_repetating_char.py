from collections import Counter

def first_unique(s):
    count =Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return -1

s = "abcbcbb"
res = first_unique(s)
print(res)