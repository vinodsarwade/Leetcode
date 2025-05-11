'''Start with the second element: Assume the first element is already sorted. 
Take the second element and compare it with the first element.
Insert the element: If the second element is smaller than the first, swap them. If not, leave them as is.
Move to the next element: Take the next element and compare it with the elements in the sorted portion of the array (from right to left).
Shift elements: Shift all elements that are greater than the current element to the right.
Insert the current element: Place the current element in its correct position.
Repeat: Repeat steps 3-5 until the entire array is sorted.'''

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while (j > 0) and (array[j] < array[j-1]):      #check if the current element is > previous element 
            array[j],array[j-1] = array[j-1],array[j]   #swap the current element with previous one
            j = j-1                                  #decrease the j to 1, and again check in while loop if condition satisfies then swap will happen.  in this way we check from right to left.
    return array

arr = [2,4,9,4,5,3,19,13]
res = insertion_sort(arr)
print(res)