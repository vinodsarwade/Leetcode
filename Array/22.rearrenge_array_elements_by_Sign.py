'''bruteforce approach O(n2)'''

'''first we seperate positive and negative elements and store in list.
then to manage order just take one element at a time from positive and negative and store in res and return.'''

#sutaible for when positive and negative elements are not equal also, for that just uncomment below code to extend res with remaining element.
def rearrange_array(arr):
    positive = []
    negative = []
    for i in range(len(arr)):
        if arr[i] > 0 :
            positive.append(arr[i])
        else:
            negative.append(arr[i])

    i = 0
    j = 0
    res = []
    while i < len(positive) and j < len(negative):
        res.append(positive[i])
        res.append(negative[j])
        i +=1
        j +=1
    # while i < len(positive):   # if elements are not equal then add remaining elements to array. 
    #     res.append(positive[i])
    #     i +=1
    # while j < len(negative):
    #     res.append(negative[j])
    #     j +=1
    return res

arr = [1,2,-3,-1,-2, 3]
# arr = [1,2,-3,-1,-2, 3, 4,5]
res = rearrange_array(arr)
print(res)

# Output:
# 1 -3  2 -1  3  -2


'''optimal approach O(n)'''
#only sutaible for when number of positive and negative elements in array are same.
'''we make sure we have one positive element then one negative element in output.
it means positive element present at index 0, 2, 4 and negative element present at 1,3,5 in o/p array.
so we are just traversing array checking if the element is postive or negative
if element is positive then put at 0th index and increase index by 2 to put next element at 2nd index
and id element is negative then put it at negative index.'''

def rearrange_array(arr):
    res = [0] * len(arr)
    posIndex = 0
    negIndex = 1
    for i in range(len(arr)):
        if arr[i] > 0:
            res[posIndex] = arr[i]
            posIndex +=2
        else:
            res[negIndex] = arr[i]
            negIndex +=2
    return res

arr = [1,2,-3,-1,-2, 3]
res = rearrange_array(arr)
print(res)
