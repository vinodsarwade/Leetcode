'''union: element those who are unique from both array in sorted order.(non-repeated)'''
# arr1 = [1,2,3,4,5,6,7,8,9,10]
# arr2 = [2,3,4,4,5,11,12]

# s = set())
# for i in range(len(arr1)):
#     s.add(arr1[i])
# for j in range(len(arr2)):
#     s.add(arr2[j])
# print(s)


'''optimal solution using two pointer approach'''
def union(arr1, arr2):
    i, j = 0, 0
    union = []
    while i < len(arr1) and j < len(arr2):             #make sure both pointer didnt go beyond length
        if arr1[i] <= arr2[j]:                         #compare array element and if small element found from arr1
            if not union or union[-1] != arr1[i]:      #then check that found element from arr1 is already present in union if not then append that element in union.
                union.append(arr1[i])                  #here we checking only last element of union array not whole union array  bcz array is sorted  so at each iteration will get bigger element.
            i+=1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1

    '''sometime array index goes beyond the range for any of the array, then to add remaining element to union'''
    for i in range(i,len(arr1)):    #check from current i to end(array1) to add reamaining element to union from arr1
        if arr1[i] not in union:    #check element is present or not in union
        # if union[-1] != arr1[i]:  # or we can check only last element in union bcz array is sorted.
            union.append(arr1[i])
    
    for j in range(j,len(arr2)):    #This is for add remainning element from arr2 
        if arr2[j] not in union:
            union.append(arr2[j])
    return union
 
arr1 = [1,2,3,4,5,6,7,8,9,10,12]
arr2 = [2,3,4,4,5,11]
res = union(arr1,arr2)
print(res)