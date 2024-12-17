#remove elements from an array
nums = [0,1,2,2,3,0,4,2]
val = 2

my_list = []
for i in nums:
    if i != val:
        my_list.append(i)
print ((my_list))

