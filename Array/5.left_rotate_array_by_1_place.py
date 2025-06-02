'''rotata array to left by 1 place'''
def left_rotate(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i] 
    arr[n-1] = temp
    return arr
    
my_array= [1,2,3,4,5]           #[2,3,4,5,1]
res = left_rotate(my_array)
print(res)    



'''rotate array to left by k places'''
def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    def swap(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start = start +1
            end = end -1

    swap(arr, 0, k-1)   
    swap(arr, k, n-1)  
    swap(arr, 0 , n-1)
    return arr

my_array= [1,2,3,4,5,6,7]    #[4,5,6,7,1,2,3]
k = 3
res = left_rotate(my_array, k)
print(res)    




''' using slicing '''
def left_rotate(arr , k):
    return arr[k:] + arr[:k]

my_array= [1,2,3,4,5,6,7]    #[4,5,6,7,1,2,3]
k = 4
res = left_rotate(my_array, k)
print(res)   


