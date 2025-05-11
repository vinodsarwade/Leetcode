def frequency_number(arr):
    frequency = {}
    for number in arr:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    max_frequemcy = max(frequency, key=frequency.get)

    return frequency,max_frequemcy
arr = [1,2,6,4,3,2,13,6,3,6]
res = frequency_number(arr)
print(res)
    

