'''using two pointer method'''
def reverse_array(arr):
    n = len(arr)
    i = 0
    j = n-1
    while (i <= j):
        arr[i], arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    return arr
arr = [1,2,3,4,5,6,7]
print(reverse_array(arr))


'''using only one pointer'''
def reverse_array(arr):
    n = len(arr)
    i = 0
    while( i <= n/2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        i+=1
    return arr
arr = [1,2,3,4,5]
print(reverse_array(arr))