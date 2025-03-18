# '''reverse array using two pointer and recurssion'''
# def reverse_array(arr,left,right):
#     if left >= right:
#         return 
#     arr[left],arr[right] = arr[right],arr[left]
#     reverse_array(arr, left+1, right-1)

# arr = [1,2,3,4,5,6,7]
# reverse_array(arr, 0, len(arr)-1)
# print(arr)


'''using recurssion with single pointer'''
def reverse_array(arr,left):
    n = len(arr)
    if left >= n/2:
        return 
    arr[left],arr[n-left-1] = arr[n-left-1],arr[left]
    reverse_array(arr, left+1)

arr = [1,2,3,4,5,6,7]
reverse_array(arr, 0)
print(arr)
