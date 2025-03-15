#input = 12321
#output = True

'''using extraction of digits'''
def check_palindrome(num):
    temp = num
    reverse_number = 0
    while(num > 0):
        last_digit = num % 10
        num = num // 10
        reverse_number = (reverse_number * 10)+ last_digit
    return (reverse_number == temp )

print(check_palindrome(121))