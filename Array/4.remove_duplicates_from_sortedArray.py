'''bruteforce approach using extra data structure '''
def remove_duplicates(arr):
    sorted_arr = []
    for i in range(len(arr)):
        if arr[i] not in sorted_arr:
            sorted_arr.append(arr[i])
    return sorted_arr

arr = [1,2,3,4,4,4,5,6]
res = (remove_duplicates(arr))
print(res)


'''optimal inplace solution'''
def remove_duplicates(arr):
    j = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[j]:
            j+=1
            arr[j] = arr[i]
    return j+1

arr = [1,2,2,3,4,4,4,5,6]
res = (remove_duplicates(arr))
print(arr[:res])



