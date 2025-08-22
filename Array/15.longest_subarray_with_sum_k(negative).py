'''bruteforce approach O(n2), same like longest_subarray with sum k (positive)'''
def longest_subarray_with_negative(arr, k):
    length = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == k:
                length = max(length, j-i+1)
    return length

arr = [1, -1, 5, -2, 3]
K = 3
print(longest_subarray_with_negative(arr ,K))
# Output: 4 (subarray: [-1, 5, -2, 3])


'''optimal solution , we can not use sliding window or two pointer here for negative element.
so use HashMap + prefix_sum  which suitable for both positive and negative elements.'''

def longest_subarray_with_negative(arr, k):
    prefix_sum = {}
    current_sum = 0
    max_len = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == k:
            max_len = max(max_len, i+1)

        rem = current_sum - k
        if rem in prefix_sum:
            max_len = max(max_len, i-prefix_sum[rem])

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = 1

    return max_len

arr = [1, -1, 5, -2, 3]
k = 3
print(longest_subarray_with_negative(arr ,k))
