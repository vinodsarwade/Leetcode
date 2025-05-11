#shuffle string
def restoreString(s: str, indices: list[int]) -> str:
        res = {}
        for char, index in zip(s,indices):
                res[index] = char
        re = ""
        for i in range(len(s)):
                re = re + res[i]
        return re
s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))

#or
# def restoreString(s: str, indices: list[int]) -> str:
#         res =[""]*len(s) 
#         for char ,index in zip(s, indices):
#             res[index] = char
#         return "".join(res)
# s = 'codeleet'
# indices = [4,5,6,7,0,2,1,3]
# print(restoreString(s, indices))