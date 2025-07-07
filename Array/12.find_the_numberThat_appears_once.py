'''better approach'''
def find_number(arr):
    my_dict = {}
    for i in range(len(arr)):
        if arr[i] not in my_dict:
            my_dict[arr[i]] = 1
        else:
            my_dict[arr[i]] +=1
    for key, value in my_dict.items():
        if my_dict[key] == 1:
            return key

arr = [4,1,2,1,2]
res = find_number(arr)
print(res)


'''optimal solution for one number appears once and other number appears twise'''
def find_number(arr):
    Xor = 0
    for i in range(len(arr)):
        Xor = Xor ^ arr[i]
    return Xor

arr = [1,2,1,4,4]
res = find_number(arr)
print(res)
