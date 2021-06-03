"""


"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rotateMatrix(matrix):

    matrixlen = len(matrix)
    print(matrix)
    for i in range(matrixlen):
        for j in range(i,matrixlen):
            matrix[j][i] , matrix[i][j] = matrix[i][j] , matrix[j][i]
    print(matrix)

    for i in range(matrixlen):
        for j in range(matrixlen//2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

    return matrix

print(rotateMatrix(matrix))
print()
print(rotateMatrix(matrix2))