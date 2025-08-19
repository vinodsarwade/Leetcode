'''bruteforce approach O(n2)'''
def subarray_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s = s + arr[j]
            if s == k:
                count +=1
    return count

array = [3, 1, 2, 4]
k = 6
res = subarray_sum(array, k)
print(res)