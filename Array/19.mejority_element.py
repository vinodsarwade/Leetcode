'''better approach using hash map'''
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


'''optimal solution using Moore voting algorithem'''

def mejority_element(arr):
    count = 0
    element = 0

    for i in range(len(arr)):   # Moore voting algo
        if count == 0:
            element = arr[i]  # at first iterration consider first item in array as element 
        if arr[i] == element: # if next item == element then increase count
            count +=1
        else:
            count -=1       # if next item not same as element then decrese count 
                            # if the count is zero it means first if condition will true and you will get new element which is arr[i] of that iteration.

    cnt = 0                    #checking the element got from above code is actually present n/2 times or not.
    for i in range(len(arr)):
        if arr[i] == element:
            cnt +=1
    if cnt > len(arr)/2:
        return element
        
arr = [2,2,3,3,1,2,2]
res = mejority_element(arr)
print(res)
