'''compare adjacent element in array if the element is in wrong order then swap them, ultimately at first 
iteration highest number will be at rightmost side ie: at last of the array.
next time you dont need to traverse up to end bcz last element already sorted so traerse uo to n-i only.

highest element to right side '''
def bubble_sort(arr):
    n = len(arr)  
    for i in range(n):  
        for j in range(1,n-i): 
            if arr[j] < arr[j-1]: 
                arr[j], arr[j-1] = arr[j-1],arr[j]
    return arr
arr = [12,25,60,35,32]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

