def nextGreaterPermutation(arr):
    breakIndex = -1
    for i in range(len(arr)-2, -1, -1):   #find the first decreasing element from reverse . right to left. that is your breakpoint.
        if arr[i] < arr[i+1]:
            breakIndex = i
            break

    if breakIndex == -1:  #if the breakpoint not found it means the array is at last permutation step. just reverse array for next permutation
        return arr.reverse()
    
    for j in range(len(arr)-1, breakIndex, -1): # then again traverse from right to breakpoint  to find  just bigger number than breakpoint.
        if arr[j] > arr[breakIndex]: # if bigger number found
            arr[breakIndex], arr[j] =  arr[j], arr[breakIndex]  #swap number with breakindex.
            break
    
    arr[breakIndex+1:] = reversed(arr[breakIndex+1:])  # at last reverse whole array from breakindex to end.

    return arr

array= [2, 1, 5, 4, 3, 0, 0]
res = nextGreaterPermutation(array)
print(res)