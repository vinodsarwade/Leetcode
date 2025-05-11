# class Solution(object):
#     def removeDuplicates(self, nums):
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return nums
#         # return len(nums) 

# obj1 = Solution()
# nums = [1,1,2]
# print(obj1.removeDuplicates(nums))


#using for loop

def remove_duplicates(nums):
    j = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[j]:
            j += 1
            # Move the unique element to the next position
            nums[j] = nums[i]

    return j + 1
nums = [1, 1, 1]
k1 = remove_duplicates(nums)
print(k1, nums[:k1])

