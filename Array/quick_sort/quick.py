# '''pythonic solution using two extra list to store left and right part'''
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = [] 
#     for i in range(1,len(arr)):
#         if arr[i] <= pivot:                  #smaller element than pivot add in left list
#             left.append(arr[i])
#         else:
#             right.append(arr[i])              #larger element than pivot add it in right list
#     sorted_left = quick_sort(left)            #then for first recurrsive call pass left array 
#     sorted_right = quick_sort(right)           #and right part too pass  , it will devide the array untill len(arr) <= 1, if the len(arr) is 1 means array is sorted.
#     return sorted_left + [pivot] + sorted_right      # and combine them 

# arr = [5,5,3,2,8,1,9]
# print(quick_sort(arr))


'''inplace solution for quick sort'''

'''quick sort works on devide and concqer  algo. in which we are going to partition the array using recurrsion in two parts
for devide/partition it in two parts we are selecting a pivot element in array and then by comparing pivot element with array elements , 
if element is less than pivot shift to left side and if element is greater than pivot shift to right side.'''
def partition_func(arr, low, high):
    pivot = arr[low]   #select pivot 
    i = low
    j = high

    while i < j:
        while i <= j and arr[i] <= pivot:    #if bigger element is found condition will false 
            i += 1
        while i <= j and arr[j] > pivot:      # if smaller element is found condition will false
            j -= 1
        if i < j:                              #check if the i not crosses j 
            arr[i], arr[j] = arr[j], arr[i]     #and we can swap than i and j element 
    arr[low], arr[j] = arr[j], arr[low]
    return j                                 #return j as a partition for nect recurrsive call
                                             #for next call again i is low and j is high ie: returned value by partition func.(left half of array from first pivot)
def quick_sort(arr, low, high):
    if low < high:
        partition = partition_func(arr, low, high)
        quick_sort(arr, low, partition-1)
        quick_sort(arr, partition +1, high)
    return arr

arr = [5,8,7,87,98,3,5,16,45]
res = quick_sort(arr, 0, len(arr)-1)
print(res)



