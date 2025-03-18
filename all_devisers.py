# '''using this approach we are traveling loop up to n times so time complexities is will be o(n)'''
# def devisers(num):
#     arr= []
#     for i in range(1, num+1):
#         if num % i == 0:
#             arr.append(i)
#     return arr
# print(devisers(36))


'''optimal solution
we dont need to traverse up to n, deviseres of number always lies between 1 to sqrt(n)
1 X 36
2 X 18
3 X 12
4 X 9
6 X 6   #we have to take numbers up to sqrt(n) it will cover all the deviseres but in unsorted order

9 X 4 
12 X 3
18 X 2
36 X 1
'''
import math
def findDivisors(n):
    divisors = [] 
    sqrtN = int(math.sqrt(n)) 
    for i in range(1, sqrtN + 1): 
        if n % i == 0:  #it will add all devisers before the sqrt(n) ie: 1,2,3,4,6
            divisors.append(i) 
            if i != (n // i): #it will add all the devisers after the sqrt(n) to n ie: 9,12,18,36
                divisors.append(n // i)  
    return sorted(divisors )
    
print(findDivisors(36))

