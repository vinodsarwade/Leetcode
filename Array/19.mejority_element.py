def mejority_element(arr):
    hash = {}
    for i in range(len(arr)):
        if arr[i] in hash:
            hash[arr[i]] +=1
        else:
            hash[arr[i]] = 1

    for key, value in hash.items():
        if value > len(arr)/2:
            return key, value
        else:
            return -1
        
arr = [2,2,3,3,1,2,2]
res = mejority_element(arr)
print(res)