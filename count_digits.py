# Input:N = 12345
# Output:5

# Input:N = 7789
# Output: 4

'''using digits of extraction '''
def count_dogits(num):
    count = 0
    while(num > 0):
        last_digit = num % 10
        num = num // 10
        count += 1
    return count
print(count_dogits(1234))

