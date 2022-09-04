# NxN의 자물쇠, 열쇠는 MxM
# 자물쇠영역을 벗어난 부분에 있는건 영향을 주지 않음. 자물쇠 영역내에서는 열쇠가 맞아 떨어져야함.
# 완전탐색으로 풀 수 있음. -> 그리고 영역의 합이 N X N을 넘어서는 안됨 딱 N x N이어야함.

# 회전하는 알고리즘. 
"""
[1, 2, 3]   [7, 4, 1] -> 2: (0,1) (1, 0) / 6: (1, 2)--> (2, 1) // 8:(2,1)-> (1,0) // 4: (1,0)->(0,1)
[4, 5, 6]   [8, 5, 2] -> 7: (2,0) ->(0,0) / 1: (0,0) -> (0,2) // 3: (0,2) -> (2,2) // 9: (2,2)->(2,0)
[7, 8, 9]   [9, 6, 3]
n_row, n_col // row, col
기존의 row들이 새로운 index인 n_col로 감 
n =3 /
0 2(0) / 0 0(0) / 2 0(2) / 2 2(2) 
1 0(1) / 2 1(2) / 1 2(1) / 0 1(0)
n_row는 n_row = col - row + 1



회전 후의 행 번호는 회전 전의 열 번호 n_row = col
회전 후의 열 번호는 N - 1에서 회전 전의 행을 뺀 것. n_col = n-1-row
# lock 주변에 m 크기만큼 더 이어 붙이기. 그래야 행렬이 돌아다니기 편함
"""

def rotate(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for row in range(m):
        for col in range(m):
            result[col][m-1-row] = key[row][col]
    return result

def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)

    board = [[0]*(n + 2 * m) for _ in range(2*m + n)]
    for i in range(n+2*m):
        for j in range(n + 2*m):
            if m <= i < m+n and m <= j < m+n:
                board[i][j] = lock[i-m][j-m]
    
    for i in range(n+m):
        for j in range(n+m):
            for k in range(4):
                key = rotate(key)
                flag = True

                for y in range(m):
                    for x in range(m):
                        board[i+y][j+x] += key[y][x]
                for y in range(m, n+m):
                    for x in range(m, n+m):
                        if board[y][x] != 1:
                            flag = False
                if flag == False:
                    for y in range(m):
                        for x in range(m):
                            board[i+y][j+x] -= key[y][x]
                else:
                    return True
    return False

# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]]	, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))