#compute cube of first n numbers using recurssion
def sum(n):
    if n < 1:
        return 0
    return (n*n*n)+ sum(n-1)
print(sum(5))


