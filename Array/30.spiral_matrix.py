def spiral_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    top = 0
    right = col -1
    bottom = row -1
    left = 0
    new_matrix = []
    #while top <= bottom and left <= right, means it has some more rows and cols at inner side
    while top <= bottom and left <= right:
        #traverse from left side to right side  
        for i in range(left, right+1):
            new_matrix.append(matrix[top][i])
        top +=1
        #traverse from  top side to bottom side
        for i in range(top, bottom+1):
            new_matrix.append(matrix[i][right])
        right -=1
        #traverse from right(bottom) side to left side , so it's reverse  so use -1
        for i in range(right, left-1, -1):
            if top <= bottom:
                new_matrix.append(matrix[bottom][i])
        bottom -=1
        #traverse from bottom(left) side to top , it is also in reverse order so -1
        for i in range(bottom, top-1, -1):
            if left <= right:
                new_matrix.append(matrix[i][left])
        left +=1
    return new_matrix
              
matrix = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
res  = spiral_matrix(matrix)
print(res)

#                   right
#    top [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]] bottom
#        left

#[ 1 2 3 4  8 12 16  15 14 13  9 5  6 7  11  10]