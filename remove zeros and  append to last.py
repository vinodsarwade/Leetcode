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
    