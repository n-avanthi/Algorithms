#hackerrank implementation
def multplication(matrix1, matrix2, matrixSize1Rows, matrixSize1Col, matrixSize2Rows, matrixSize2Col):
    resultantMatrix = []
    countAdd=0
    countMultiply=0
    for i in range(matrixSize1Rows):
        resultantRow = []
        for j in range(matrixSize2Col):
            dot_product = 0
            for k in range(matrixSize1Col):
                dot_product += matrix1[i][k] * matrix2[k][j]
                countMultiply +=1
                countAdd +=1   
            countAdd -= 1
            resultantRow.append(dot_product)
        resultantMatrix.append(resultantRow)
    for row in resultantMatrix:
        print(' '.join(map(str, row)))
    print(countMultiply, countAdd)
#main
matrixSize1 = list(map(int, input("Enter matrix size 1: ").split()))
matrixSize1Rows = matrixSize1[0]
matrixSize1Col = matrixSize1[1]
matrix1 = []

for i in range(matrixSize1Rows):
    row1 = list(map(int, input("Enter row: ").split()))
    matrix1.append(row1)

matrixSize2 = list(map(int, input("Enter matrix size 2: ").split()))
matrixSize2Rows = matrixSize2[0]
matrixSize2Col = matrixSize2[1]
matrix2 = []

for j in range(matrixSize2Rows):
    row2 = list(map(int, input("Enter row: ").split()))
    matrix2.append(row2)

if(matrixSize1Col != matrixSize2Rows):
    print("-1")
else:
    multplication(matrix1, matrix2, matrixSize1Rows, matrixSize1Col, matrixSize2Rows, matrixSize2Col)
