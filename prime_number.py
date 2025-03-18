'''bruitforce approach with o(n) time complexity'''
# def check_prime(n):
#     if n <= 1:
#         return 1
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True

# print(check_prime(11))


'''optimal solution'''
# def check_prime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     sqrt = int(n**0.5)
#     print(sqrt)
#     for i in range(5,sqrt+1,2): #step size of 2 to check only with odd numbers. loop start from 5,7,9
#         if n % i == 0:
#             return False
#     return True
# print(check_prime(37))


'''another optimal solution'''
import math
def check_prime(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1): 
        if n % i == 0:  
            count+= 1
            if i != (n // i): 
                count+=1
    if count == 2:
        return True
    else:
        return False
print(check_prime(37))