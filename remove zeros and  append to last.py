class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """            
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count +=1
            else:
                i  += 1
        nums += ([0]*count)


    
# remove zeros and append it to last in array using while loop
nums = [0,1,0,3,12]
count = 0
i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
        count +=1
    else:
        i  += 1
print(nums + ([0]*count))



#using for loop
nums = [0,1,0,3,0,0,12]
my_list = []
count = 0
for i in nums:
    if i == 0:
        count += 1
    else:
        my_list.append(i)
print(my_list + [0]*count)



'''remove all zeros and append at last of array'''
def remove_zero(my_list):
    new_list = []
    count = 0
    for number in my_list:
        if number == 0:
            count += 1 
        else:
            new_list.append(number)
    new_list.extend([0] * count)
    return new_list

my_list = [1,2,0,5,6,0,3,0]
res = remove_zero(my_list)
print(res)
    