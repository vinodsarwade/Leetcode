class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return nums
        # return len(nums) 

obj1 = Solution()
nums = [1,1,2]
print(obj1.removeDuplicates(nums))


#using for loop

def remove_duplicates(nums):
    unique_index = 0
    for i in range(1,len(nums)):     
        if nums[i] != nums[unique_index]:
            unique_index += 1
            # Move the unique element to the next position
            nums[unique_index] = nums[i]

    return unique_index + 1
nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print(k1, nums1[:k1])

