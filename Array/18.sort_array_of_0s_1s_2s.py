'''bruteforce solution pythonic approach'''
def sort_array(arr):
    return sorted(arr)

arr = [0,0,2,1,2,1,0,0,2,1]
res = sort_array(arr)
print(res)


'''better approach O(2N)'''
def sort_array(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count_0 +=1
        elif arr[i]== 1:
            count_1 +=1
        else:
            count_2+=1
    return [0]*count_0 + [1]*count_1 + [2]*count_2

arr = [0,0,2,1,2,1,0,0,2,1]
res = sort_array(arr)
print(res)



'''optimal solution  TC = O(N), SC = O(1)
using dutch national flag alogorithem 

This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

arr[0….low-1] contains 0. [Extreme left part]
arr[low….mid-1] contains 1.
arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
The middle part i.e. arr[mid….high] is the unsorted segment. 


First, we will run a loop that will continue until mid <= high.
There can be three different values of mid pointer i.e. arr[mid]
If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
Finally, our array should be sorted.'''

def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while (mid <= high):
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low +=1
            mid +=1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid], arr[high] = arr[high],arr[mid]
            high -= 1
    return arr
arr = [0,0,2,1,2,1,0,0,2,1]
res = sort_array(arr)
print(res)