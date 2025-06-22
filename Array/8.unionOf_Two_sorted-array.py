# arr1 = [1,2,3,4,5,6,7,8,9,10]
# arr2 = [2,3,4,4,5,11,12]

# s = set()
# for i in range(len(arr1)):
#     s.add(arr1[i])
# for j in range(len(arr2)):
#     s.add(arr2[j])
# print(s)


'''optimal solution'''
def union(arr1, arr2):
    i, j = 0, 0
    union = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1

    for i in range(i,len(arr1)):
        if arr1[i] not in union:
            union.append(arr1[i])
    
    for j in range(j,len(arr2)):
        if arr2[j] not in union:
            union.append(arr2[j])
    return union
 
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
res = union(arr1,arr2)
print(res)