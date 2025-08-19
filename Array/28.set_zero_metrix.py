def set_matrix_zero(matrix):
    row = len(matrix)      #len of matrix is our row
    col = len(matrix[0])   # matrix[0] means first array is our column    1  1  1
#                                                                            1  0  1
#                                                                            1  1  1
    '''approach- first we traversing the matrix using two loops, everytime to traverse matrix it require
    two loop so time complexity is On2. so when we traverse the matrix by each element, when the  0 element is found
    we are assigning -1 to  the column and row as per first loop.
    and at second loop we are just traversing the matrix again , and check wherever the -1 is present just replace that -1 to 0
    at end your zeros will be set in matrix.'''
    row_zero = [0] * row  #we are creating extra row and col to store -1 if 0 found. for just keeping track of 0
    col_zero = [0] * col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row_zero[i] = -1
                col_zero[j] = -1

    #then by using tracked zeros in zero_row and zero_col just replaced -1 to 0        
    for i in range(row):
        for j in range(col):
            if row_zero[i] == -1 or col_zero[j] == -1:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
res = set_matrix_zero(matrix)
print(res)