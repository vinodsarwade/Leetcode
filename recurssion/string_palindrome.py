def check_palindrome(i,s):
    n = len(s)
    if i >= n/2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return check_palindrome(i+1,s)
    
s= "madam"
print(check_palindrome(0,s))