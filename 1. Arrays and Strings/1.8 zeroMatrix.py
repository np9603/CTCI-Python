"""


"""

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def zeroMatrix1(matrix):

    print(matrix)
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])

    zero_row = [False] * m
    zero_col = [False] * n

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zero_row[row] = True
                zero_col[col] = True

    for row in range(m):
        for col in range(n):
            if zero_row[row] or zero_col[col]:
                matrix[row][col] = 0

    return matrix

print(zeroMatrix1(matrix))
print()
print(zeroMatrix1(matrix2))

matrix3 = [[1,1,1],[1,0,1],[1,1,1]]
matrix4 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def zeroMatrix2(matrix):

    print(matrix)
    col0 = 1
    rows , cols = len(matrix), len(matrix[0])

    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(rows-1,-1,-1):
        for j in range(1,cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0

    return matrix



print()
print(zeroMatrix2(matrix3))
print()
print(zeroMatrix2(matrix4))