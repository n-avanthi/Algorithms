def matrix_addition(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return -1
    
    result = []
    addition_count = 0

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            sum_element = mat1[i][j] + mat2[i][j]
            row.append(sum_element)
            addition_count += 1
        result.append(row)
    
    return result, addition_count

# Input dimensions for matrix 1
rows1, cols1 = map(int, input().split())
matrix1 = []
for _ in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input dimensions for matrix 2
rows2, cols2 = map(int, input().split())
matrix2 = []
for _ in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = matrix_addition(matrix1, matrix2)

if result == -1:
    print(result)
else:
    for row in result[0]:
        print(" ".join(map(str, row)))
    print(result[1])