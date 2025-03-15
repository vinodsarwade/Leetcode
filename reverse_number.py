# Example 1:
# Input:N = 12345
# Output:54321
# Explanation: The reverse of 12345 is 54321.
# Example 2:
# Input:N = 7789
# Output: 9877
# Explanation: The reverse of number 7789 is 9877.

def reverse_number(num):
    rev_number = 0
    while num > 0:
        last_digit = (num % 10)
        num = num // 10
        rev_number = (rev_number * 10)+last_digit
    return rev_number

res = reverse_number(12345)
print(res)