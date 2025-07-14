'''Given an array and a sum k, we need to print the length of the longest subarray that sums to k.'''

'''bruteforce approach  O(n3)'''
def longest_subarray(arr, k):
    length = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for p in range(i, j+1):
                sum += arr[p]
            if sum == k:
                length = max(length, j-i+1)
    return length

arr = [2, 3, 5, 1, 9]
k = 10
res = longest_subarray(arr, k)
print(res)



'''Bruteforce O(n2)'''
#here we are just adding j in sum and each time checking if the sum is equals to K . if equals then update the length.
def longest_subarray(arr, k):
    length = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum +=arr[j]
            if sum == k:
                length = max(length, j-i+1)
    return length

arr = [2, 3, 5, 1, 9]
k = 10
res = longest_subarray(arr, k)
print(res)


'''optimal approach two pointer sliding window
here we traversing array and adding sum to current_sum, if the current_sum is > K then we just shrinking element from left side means from starting from the array
until the current_sum is <= K.
if the current_sum is == k then we just finding the length of subarray using i-j+1

#usefull only for positive array , bcz shrinking element not guarantee to decrease the sum bcz negative element..
'''
def longest_subarray(arr, k):
    j = 0
    max_len = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]

        while current_sum > k :
            current_sum = current_sum - arr[j]
            j +=1

        if current_sum == k:
            max_len = max(max_len, i-j+1)
    return max_len

arr = [3, 3, 5, 2, 9]
k = 10
res = longest_subarray(arr, k)
print(res)