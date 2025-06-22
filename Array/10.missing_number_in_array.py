def missing_number_inArray(arr):
    sum = 0
    total_sum = 0
    for i in range(len(arr)):
       sum += arr[i]

    for i in range(1, len(arr)+2):
        total_sum += i
    return  total_sum - sum


arr = [1,2,4,5]
res  = missing_number_inArray(arr)
print(res)