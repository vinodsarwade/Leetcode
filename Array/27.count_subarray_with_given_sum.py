'''bruteforce approach O(n2)'''
def subarray_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s = s + arr[j]
            if s == k:
                count +=1
    return count

array = [3, 1, 2, 4]
k = 6
res = subarray_sum(array, k)
print(res)


'''optimal solution using prefix_sum and hashmap O(n) '''
def subarray_sum(array , k):
    count = 0
    prefix_sum = {0:1} 
    current_sum = 0
    for i in range(len(array)):
        current_sum = current_sum + array[i]

        rem = current_sum - k
        if rem in prefix_sum:
            count = count + prefix_sum[rem]

        if current_sum in prefix_sum:
            prefix_sum[current_sum] = prefix_sum[current_sum]+1
        else:
            prefix_sum[current_sum] = 1

    return count

array = [3, 1, 2, 4]
k = 6
res = subarray_sum(array, k)
print(res)