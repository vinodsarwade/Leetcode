def frequency_number(arr):
    frequency = {}
    for number in arr:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # max_frequemcy = max(frequency, key=frequency.get)
    # return frequency,max_frequemcy
            
    count = 0
    number = 0 
    for i in frequency:                  #once we get frequency dict we can find max number and count in this way also by traversing dict.
        if frequency[i] > count:
            count = frequency[i]
            number = i
    return f"{number} is present {count} times"
    
arr = [1,2,6,4,3,2,13,6,3,3,3,6]
res = frequency_number(arr)
print(res)
    

