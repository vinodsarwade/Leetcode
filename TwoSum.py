'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution():
    def TwoSum(self, num, target):
        dic = {}                           #{2:0}
        for index, value in  enumerate(num):  #0, 2     1,7
            n= target - value                 #9-2 =7   9-7=2
            if n in dic:
                return dic[n], index
            dic[value] = index


obj1 = Solution()
num = [2,7,11,15]
target = 9
print(obj1.TwoSum(num, target))


