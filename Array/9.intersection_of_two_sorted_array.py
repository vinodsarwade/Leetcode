'''intersection: element who present in both array corruspondingly'''
'''bruteforce approach'''
def intersection(arr1, arr2):
    intersection_array = []
    visited_array = [0] * len(arr2)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and visited_array[j] == 0:
                intersection_array.append(arr1[i])
                visited_array[j] = 1
                break

    return intersection_array

arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]
res = intersection(arr1, arr2)
print(res)


'''optimal solution using two pointer approach'''
def intersection(arr1, arr2):
    i, j = 0, 0
    intersection_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i +=1
        elif arr1[i] > arr2[j]:
            j +=1
        else:
            intersection_array.append(arr1[i])
            i +=1
            j +=1
    return intersection_array
arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]
res = intersection(arr1, arr2)
print(res)
