'''find number of subbarrays in given array which equals to given sum.
find the number of subarray's which equals to the sum K 
'''

def longest_subarray(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            s = 0
            for p in range(i, j+1):
                s = s + arr[p]
            if s == k:
                count += 1
    return count

arr = [2, 3, 5, 1, 9]
k = 10
res = longest_subarray(arr, k)
print(res)