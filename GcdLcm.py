# ''' bruteforce approach is to traverse min(a,b) to find GCD of a given numbers.
# using for loop we can traverse up to minimum number between a and b and using if condition we can check if the 
# both a and b are devided by same deviser then return this deviser. time complexity is higher o(log(min(a,b)))'''
# #bruteforce approach
# def findGCD(a, b):
#     gcd = 1
#     for i in range(min(a,b),0, -1):
#         if (a % i == 0) and (b % i == 0):
#             gcd = i
#             break
#     return gcd
# print(findGCD(6,16))

# #optimal solution  using Euclidean algorithem
# def findgcd(a, b):
#     while( a > 0 and b > 0):
#         if (a > b):    #wrather than checking  condition each time which number is smaller and greater we can directly swap the number like below example
#             a = a%b
#         else:
#             b = b%a
#     if (a == 0):
#         return b
#     else:
#         return a
# print(findgcd(12,16))


# '''optimal solution using Euclidean algorithem'''
# gcd(a,b) == gcd(b, a%b)
def lcmAndGcd(a : int, b : int) -> list[int]:
        def gcd(a,b):
            while(b != 0):
                a,b = b, a%b   #euclidean algorithem (here after swapping always a>b and once b is 0 it will return a)
            return a

        def lcm(a,b):
            k= gcd(a,b)
            var = (a*b) // k  
            return var
        return [lcm(a,b), gcd(a,b)]
print(lcmAndGcd(12,16))



