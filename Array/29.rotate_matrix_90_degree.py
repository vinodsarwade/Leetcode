'''bruteforce solution'''
# input_matrix = [                        
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# output_matrix = [
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]]
# if you observerd this first row in the i/p matrix will be last col in o/p matrix.
#second row in i/p matrix will be second last  col in  o/p.
'''so in bruteforce approach we are creating extra matrix of same size in which we can put element.''' 
def rotate_matrix(matrix):
    n = len(matrix)
    rotate = [[0] * n for i in range(n)]   #extra matrix with intially zeros

    for i in range(n):    # traver the matrix and catch each element and put at it's correct position.
        for j in range(n):
            rotate[j][n-1-i] = matrix[i][j] 
    return rotate

input_matrix = [                        
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = rotate_matrix(input_matrix)
print(res)



'''optimal solution using transpose of matrix'''
#transpose of matrix means, converting rows to column and column to rows 
# input_matrix = [                        
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# [1, 4, 7]   # after traspose of matrix rows are converted to col and , col are converted to rows.
# [2, 5, 8]   #for our o/p just reverse each row you will get final o/p 
# [3, 6, 9]

#output_matrix = [
# [7, 4, 1]    #after reversing the each row final o/p 
# [8, 5, 2]
# [9, 6, 3]
# ]

def rotate_matrix(matrix):
    n = len(matrix)
    #transpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #reverse transpose matrix using two pointer
    for i in range(n):
        start = 0
        end = n-1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start +=1
            end -=1
    return matrix

input_matrix = [                        
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = rotate_matrix(input_matrix)
print(res)