'''bryteforce approach O(n2)'''
def longest_consecutive(arr):
    max_len = 0
    for num in arr:
        current = num
        streak = 1

        while current + 1 in arr:
            current = current + 1
            streak = streak + 1
        max_len = max(max_len, streak)
    return max_len

arr = [100, 4, 200, 1, 3, 2]
res = longest_consecutive(arr)
print(res)

'''optimal solution using set  to avoid duplicates '''
def longest_consecutive(arr):
    set_num = set(arr)
    max_len = 0

    for num in set_num:
        if num - 1 not in set_num:
            current = num
            streak = 1

        while current + 1  in set_num:
            current = current + 1
            streak = streak + 1
        max_len = max(max_len, streak)
    return max_len
arr = [100, 4, 200, 1, 3, 2]
res = longest_consecutive(arr)
print(res)