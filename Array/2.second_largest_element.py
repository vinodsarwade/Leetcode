'''bruteforce solution'''
def second_largest_element_in_array(arr):
    '''first find max element and then by comparing it with whole array find second largest'''
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
    '''declare two var for largest and second_largest and on the fly we are comparing both largest and
    second_largest element with array element,'''
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest :               #if greater element found then update it to largest and previous largest is  now second_largest
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:    # but if element in array is not > largest element, but it is greater than second largest then update only second_largest element.
            second_largest = arr[i] 
    return second_largest

arr = [4,5,6,2,6,12,12,18,18,13]
print(second_largest_element_in_array(arr))