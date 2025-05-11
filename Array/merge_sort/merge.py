'''first devide the array using resursion in two parts , left part and right part.'''
def devide_array(arr):
    if len(arr) <= 1:  #check if the array has only one element means array is already sorted
        return arr
    mid_array = len(arr) // 2       #to devide array find mid index off the array 
    left_half = devide_array(arr[:mid_array]) #using slicing call recursively devide function by passing half part of array. 0th index to mid index for left half
    right_half = devide_array(arr[mid_array:])   #same as left but now we pass right part to devide the array
    return merge(left_half, right_half)     #once devide is done call merge func by passing each part  


def merge(left_half, right_half):
    sorted_array = []
    i = 0
    j = 0
    #to merge array first we check length of both part ,and merge by comparing both arr elements up to the length of arr ie: untill i is greater than len(leftarr)
    while i < len(left_half) and j < len(right_half):   #condition is true up to len(left)and len(right)part.
        if left_half[i] <= right_half[j]:               #compare first element from both array if left element is small 
            sorted_array.append(left_half[i])           #then append it to sorted array
            i +=1
        else:
            sorted_array.append(right_half[j]) #otherwise append right element in array.
            j+=1
    
    #at some point at last either left part or right part array is end and while loop is false but remain element from the array we can add using extend 
    sorted_array.extend(left_half[i:])   #if left array element is remain then add remaining element from i to len(left part)
    sorted_array.extend(right_half[j:])   #if right array element is remain then add remain element from j to len(right part)
    return sorted_array

arr = [3, 5, 6, 32, 34, 224, 66, 44, 66, 7, 7,78,54,3,3,56,888,6,44]
res = devide_array(arr)
print(res)



