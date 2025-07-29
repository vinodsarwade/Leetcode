'''to find hills and vally first we need to remove consecutive duplicates in array bcz they are not vally and hills. '''
def hill_and_vally(arr):
    new_arr = [arr[0]]
    hill = 0
    vally = 0
    for i in range(1,len(arr)): #traversing from 1 so we defualtly add arr[0] in new_arr.
        if arr[i] != arr[i-1]:
            new_arr.append(arr[i])  # remove consecutive duplicates and append in new_arr

    for i in range(1, len(new_arr)-1):
        if new_arr[i] > new_arr[i-1] and new_arr[i] > new_arr[i+1]: #if arr[i] > than neighbour element then is hills
            hill +=1
        elif new_arr[i] < new_arr[i-1] and new_arr[i] < new_arr[i+1]: # if arr[i] < than neighbour element then it's vally
            vally +=1
    return hill + vally

arr = [2,4,1,1,6,5]
res = hill_and_vally(arr)
print(res)