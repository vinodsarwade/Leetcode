'''merge two sorted list'''
'''simply merge two sorted list with all the elements'''
def merge_two_sorted_list(arr1,arr2):
    i = 0
    j = 0
    new_array = []
    while i < (len(arr1)) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_array.append(arr1[i])
            i = i+1
        else:
            new_array.append(arr2[j])
            j = j+1

    for i in range(i, len(arr1)):
        new_array.append(arr1[i])
    for j in range(j, len(arr2)):
        new_array.append(arr2[2])
    return new_array

arr1 = [1,3,5,6,7,9]
arr2 = [1,2,3,4,5,6,7,8]
res = merge_two_sorted_list(arr1, arr2)
print(res)



'''merge two sorted list without using duplicates '''
def merge_two_sorted_list(arr1,arr2):
    i = 0
    j = 0
    new_array = []
    while i < (len(arr1)) and j < len(arr2):
        if arr1[i] <= arr2[j] :
            if arr1[i] not in new_array:
                new_array.append(arr1[i])
            i = i+1

        elif arr1[i] > arr2[j] :
            if arr2[j] not in new_array:
                new_array.append(arr2[j])
            j = j+1

    for i in range(i, len(arr1)):
        if arr1[i] not in new_array:
            new_array.append(arr1[i])
    for j in range(j, len(arr2)):
        if arr2[j] not in new_array:
            new_array.append(arr2[j])
    return new_array

arr1 = [1,3,5,6,7,9]
arr2 = [1,2,3,4,5,6,7,8,9,10,11,12,12]
res = merge_two_sorted_list(arr1, arr2)
print(res)




