'''bruteforce solution'''
def second_largest_element_in_array(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] < max and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest

arr = [4,5,6,2,6,12,12,18,18,13]
print(second_largest_element_in_array(arr))


'''optimised approach'''
def second_largest_element_in_array(arr):
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest :
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i] 
    return second_largest

arr = [4,5,6,2,6,12,12,18,18,13]
print(second_largest_element_in_array(arr))