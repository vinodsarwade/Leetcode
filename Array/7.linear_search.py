def linearSearch( nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1

print(linearSearch([2, 3, 4, 5, 3], target=2))