# '''bruteforce solution using extra space'''
# def move_zeros(arr):
#     new_arr = []
#     count = 0
#     for i in arr:
#         if i != 0:
#             new_arr.append(i)
#         else:
#             count +=1
#     new_arr.extend([0] * count)
#     return new_arr

# arr = [1,2,0,0,4,2,0,6,7]
# res = move_zeros(arr)
# print(res)


'''optimal solution '''
def move_zeros(arr):
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != 0:
            j+=1
            arr[j] = arr[i]

    for k in range(j+1, len(arr)):
        arr[k] = 0
    return arr
arr = [1,2,0,0,4,2,0,6,7]
res = move_zeros(arr)
print(res)


'''more optimal solution'''
def move_zeros(arr):
    j = 0     
    n = len(arr)        
    for i in range(n):    #here we found first 0 element and assign index of first 0 to j pointer 
        if arr[i] == 0:
            j = i
            break

    for k in range(j+1, n):  #then traverse from j to n and swap non zero element with 0 which is j.
        if arr[k] != 0:
            arr[j], arr[k] = arr[k], arr[j]
            j +=1
    return arr

arr = [1,2,0,0,4,2,0,6,7]
res = move_zeros(arr)
print(res)