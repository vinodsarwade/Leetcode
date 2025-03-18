'''check string is a palindrome or not using two pointer'''
def palindrome(s):
    n = len(s)
    i  = 0
    j = n-1
    while (i <= j):
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True 
s = "madsm"
print(palindrome(s))



'''using single pointer'''
def palindrome(s):
    n = len(s)
    i  = 0
    while (i <= n/2):
        if s[i] != s[n-i-1]:
            return False
        i+=1
    return True 
s = "madam"
print(palindrome(s))
