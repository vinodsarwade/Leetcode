'''bruteforce approach O(n2)'''
def leader_array(arr):
    new_array = []

    for i in range(len(arr)):
        leader = True
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            new_array.append(arr[i])
    return new_array

arr = [10, 22, 12, 3, 0, 6]
res = leader_array(arr)
print(res)

'''optimal solution O(n)
we need to find the element whos right side elements are smaller. 
last element in arr is always a leader so add this last element default. and then traverse from second last element.
so we traverse from right , and check if the next element is bigger then this is max_ele and append to new_arry.
and update max_ele to check for next iteration.'''
def leader_array(arr):
    new_array = []
    max_ele = arr[len(arr)-1]
    new_array.append(max_ele)
    
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_ele:
            new_array.append(arr[i])
            max_ele = arr[i]
    return new_array

arr = [10, 22, 12, 3, 0, 6]
res = leader_array(arr)
print(res)