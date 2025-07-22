'''bruteforce you can do using 3 loops same as problem no 14'''

'''better solution O(n2)'''
def maximum_subarray(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        s = 0 
        for j in range(i, len(arr)):
            s += arr[j]
            max_sum = max(s, max_sum)
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(maximum_subarray(arr))


'''optimal solution using  kadane's algo O(n)'''

'''first consider max_sum as a smallest number , then iterate over array using single loop and store sum in s
if the sum > greater than zero then update max_sum.
but if sum < 0 means negative , then negative element should not be the maximum_subarray _sum
so again update sum to 0 and iterate through next element.
basically when you find first positive number in array then only sum will be added and consider for next iter.'''

def maximum_subarray(arr):
    max_sum = float('-inf')
    s = 0
    for i in range(len(arr)):
        s += arr[i]
        if s > max_sum:
            max_sum = s
        if s < 0:
            s = 0
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(maximum_subarray(arr))
