def max_consecutive_ones(arr):
    max_count = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count +=1
        else:
            count = 0
        max_count = max(max_count,count)
    return max_count

arr = [1,1,0,1,1,1,0,1,1]
res = max_consecutive_ones(arr)
print(res)