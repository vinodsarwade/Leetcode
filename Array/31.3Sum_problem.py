'''bruteforce approach O(n3)'''
'''Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero.
In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] 
such that i!=j, j!=k, k!=i, and their sum is equal to zero.'''

def three_Sum(arr):
    result = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    tup = tuple(sorted([arr[i], arr[j], arr[k]]))
                    result.add(tup)
    res = []
    for i in result:
        res.append(list(i))
    return res

arr = [-1, 0, 1, 2, -1, -4]
res = three_Sum(arr)
print(res)


'''Better solution O(n2)'''
'''we know we need to find an three numbers in array which sums equals to zero. for that we use three loops in bruteforce solution, but to avoid third loop we can use one simple maths
if ex: arr[i]+ arr[j] = 4, then i need  -4 as a third number then only sum of three numbers equals to zero.
so arr[i]+ arr[j]+ third = 0 , to get this we can do like this, third = -(arr[i]+arr[j])
 (-1 + 0) = -1   if we add minus ie: -(-1) ==> (1), so 1 is our third number , so if third number is present in hashset then we found our three number which sums to 0.
'''
def three_sum(arr):
    st = set()
    for i in range(len(arr)):
        hashset = set()
        for j in range(i+1, len(arr)):
            third_number = -(arr[i] + arr[j])
            if third_number in hashset:
                tup = tuple(sorted([arr[i], arr[j],third_number]))
                st.add(tup)
            hashset.add(arr[j])

    res = []
    for i in st:
        res.append(list(i))
    return res

arr = [-1, 0, 1, 2, -1, -4]
res = three_sum(arr)
print(res)


'''optimal solution O(n)'''
def three_sum(arr):
    pass

arr = [-1, 0, 1, 2, -1, -4]
res = three_sum(arr)
print(res)




