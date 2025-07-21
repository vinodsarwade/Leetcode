'''bruteforce solution'''
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

arr = [2, 6, 5, 8, 11]
target = 14
res = two_sum(arr, target)
print(res)


'''optimal solution using hash map '''
def two_sum(arr, target):
    my_dict = {}
    for index , value in enumerate(arr):
        rem = target - value
        if rem in my_dict:
            return my_dict[rem], index
        else:
            my_dict[value] = index

arr = [2, 6, 5, 8, 11]
target = 14
res = two_sum(arr, target)
print(res)
