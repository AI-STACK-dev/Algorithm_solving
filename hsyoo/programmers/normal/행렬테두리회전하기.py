import copy

def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    mat = [[0] * m for _ in range(n)]
    result = int(1e9)
    for i in range(n):
        for j in range(m):
            if i == 0 and (1 <= j <= m-1):
                mat[i][j] = matrix[i][j-1]
            elif j == m-1 and 1<=i<=n-1:
                mat[i][j] = matrix[i-1][j]
            elif i == n-1 and 0<=j<m-1:
                mat[i][j] = matrix[i][j+1]
            elif j == 0 and 0 <= i < n-1:
                mat[i][j] = matrix[i+1][j]
            else:
                mat[i][j] = matrix[i][j]
    for i in range(n):
        for j in range(m):
            if mat[i][j] != matrix[i][j]:
                result = min(result, mat[i][j])
    return result, mat

def solution(rows, columns, queries):
    answer = []
    matrix = []
    num = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(num)
            num += 1
        matrix.append(temp)
    for query in queries:
        row_temp = []
        y1,x1,y2,x2 = query
        for i in range(y2-y1 + 1):
            column_temp = []
            for j in range(x2-x1+1):
                column_temp.append(matrix[i+y1-1][j+x1-1])
            row_temp.append(column_temp)
        
        value, mat_temp = rotate(row_temp)
        answer.append(value)
        for i in range(y2-y1+1):
            for j in range(x2-x1+1):
                matrix[i+y1-1][j+x1-1] = mat_temp[i][j]

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	))