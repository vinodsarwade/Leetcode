def printNos(n):
    if n < 1: #here we are checking in reverse order once condition is false recursion will be printed 
        return
    printNos(n-1)
    print(n,end=" ")
printNos(10)


# def printNos(n):
#     if n < 1: 
#         return
#     print(n,end=" ")   #printing in reverse order we are printing before the recurssive call itself.
#     printNos(n-1)
# printNos(10)


#or
def printNos(count, n):    #here we are setting count var to 1 once count > n condition is false 
    if count > n:
        return
    print(count,end=" ")   #each time we checking condition and printing count and again call to fun by incrementing count.
    printNos(count+1, n)
printNos(1, 10)