'''using extraction of digits'''
def armstrong(num):
    temp = num
    sum = 0
    while(num > 0):
        last_digit = num % 10 
        num = num // 10
        sum = sum + (last_digit*last_digit*last_digit)
    if sum == temp:
        return True
    else:
        return False

print(armstrong(371))