'''bruteforce approach O(n2)'''
def maxprofit(arr):
    maxProfit = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                maxProfit = max(maxProfit, arr[j]-arr[i])
    return maxProfit

arr = [7, 1, 5, 3, 6, 4]
res= maxprofit(arr)
print(res)


'''optimal appraoch'''
def maxprofit(arr):
    maxProfit = 0
    buy_price = float('inf')
    for i in range(len(arr)):
        if arr[i] < buy_price:
            buy_price = arr[i]
        # buy_price = min(buy_price, arr[i])   #you can replace above two lines with this single line to find min buy_price.
        maxProfit = max(maxProfit, arr[i]- buy_price)
    return maxProfit

arr = [7, 1, 5, 3, 6, 4]
res= maxprofit(arr)
print(res)


'''optimal solution using while loop'''
def maxprofit(arr):
    maxProfit = 0
    buy_price = float('inf')
    i = 1
    while i < len(arr):
        if arr[i] < buy_price:
            buy_price = arr[i]
        else:
            maxProfit = max(maxProfit, arr[i]-buy_price)
        i +=1
    return maxProfit

arr = [7, 1, 5, 3, 6, 4]
res= maxprofit(arr)
print(res)
