'''consider minimum element from an array, then traverse to end of an array ie: n, at each iteration we will get 
small value at left most side ie: first element in array.
for 2nd pass u dont need to traverse from first bcz first element is already small and sorted. so traverse from (i+1 to n)

smallest element to left side.'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr
arr = [12,25,11,6]
sorted_arr = selection_sort(arr)
print(sorted_arr)