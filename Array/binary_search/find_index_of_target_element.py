# Input:
# arr = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 7

# Output:
# 3

''' uses two pointer method one pointer at 0th index and another at end of array
find mid of array, & compare mid to target if mid and target is same then return mid
if the mid is < target then move left ptr to mid+1, and if the mid > target then move right to mid-1 '''
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right= mid - 1
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

res = binary_search(arr, target)
print(res)
