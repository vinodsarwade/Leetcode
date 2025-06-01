'''pythnoic solution'''
def largest_element_in_array(arr):
    arr.sort()
    return arr[-1]

arr = [4,5,6,2,6,12,18]
print(largest_element_in_array(arr))



'''using bubble sort '''
def largest_element_in_array(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1],arr[j]
    return arr[-1]

arr = [4,5,6,2,6,12,18]
print(largest_element_in_array(arr))



'''optimised'''
def largest_element_in_array(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [4,5,6,2,6,12,18]
print(largest_element_in_array(arr))
