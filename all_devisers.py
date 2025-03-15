# '''using this approach we are traveling loop up to n times so time complexities is will be o(n)'''
# def devisers(num):
#     arr= []
#     for i in range(1, num+1):
#         if num % i == 0:
#             arr.append(i)
#     return arr
# print(devisers(36))


import math
def findDivisors(n):
    divisors = [] 
    sqrtN = int(math.sqrt(n)) 
    for i in range(1, sqrtN + 1): 
        if n % i == 0: 
            divisors.append(i) 
            if i != n // i:
                divisors.append(n // i) 
    return sorted(divisors )
    
print(findDivisors(12))

