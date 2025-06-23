'''bruteforce solution'''
# def missing_number_inArray(arr):
#     sum = 0
#     total_sum = 0
#     for i in range(len(arr)):
#        sum += arr[i]

#     for i in range(1, len(arr)+2):
#         total_sum += i
#     return  total_sum - sum


# arr = [1,2,4,5]
# res  = missing_number_inArray(arr)
# print(res)

# '''optimal solution'''
# def missing_number_inArray(arr):
#     sum = 0
#     n = len(arr)+1
#     for i in range(len(arr)):
#         sum += arr[i]

#     total_sum = (n *(n+1)/2)
#     return total_sum - sum

# arr = [1,2,4,5]
# res  = missing_number_inArray(arr)
# print(res)


'''more optimal solution using Xor'''

def missing_number_Xor(arr):
    Xor_full = 0
    Xor_arr = 0
    n = len(arr)+1
    for i in range(1,n+1):
        Xor_full = Xor_full ^ i        # 1 ^ 1 = 0   if same number then Xor = 0
    for num in arr:                    # 2 ^ 2 = 0
        Xor_arr = Xor_arr ^ num        # 1 ^ 0 = 1   if Xor with 0 then that number will be Xor.
    return Xor_full ^ Xor_arr

arr = [1,2,4,5]
res = missing_number_Xor(arr)
print(res)