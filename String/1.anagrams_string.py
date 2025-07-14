'''bruteforce approach '''
def check_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True
str1 = "INTEGER"
str2 = "TEGERNI"

res = check_anagrams(str1, str2)
print(res)
  
