
def sorted(arr):
    for i in range(1, len(arr)):
        if arr [i] < arr[i-1]:
            return False
    return True

arr = [3,4,5,5,6,]
print(sorted(arr))