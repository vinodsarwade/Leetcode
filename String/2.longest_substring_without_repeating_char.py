def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        hash = {}
        for j in range(i, n):
            if s[j] in hash:
                break
            hash[s[j]] = 1

            length = j - i + 1
            max_len = max(length, max_len)
    return max_len

s = "abcabcbb"
res = length_of_longest_substring(s)
print(res)
                        

'''optimal'''
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

s = "abcabcbb"
res = length_of_longest_substring(s)
print(res)
           