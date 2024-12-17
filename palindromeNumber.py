class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            x_str = str(x)                    #convert to string
            new = x_str[:: -1]                #reverse the string
            return x_str == new               #check for both string same or not and return boolen
            # return x_str == x_str[::-1]     #above two lines in single line


# obj1 = Solution()
# num = 121
# print(obj1.isPalindrome(num))