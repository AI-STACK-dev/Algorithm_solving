# def rotate(key):
#     row_length = len(key)
#     column_length = len(key[0])
#     n_board = [[0] * row_length for _ in range(column_length)]

#     for r in range(row_length):
#         for c in range(column_length):
#             n_board[c][row_length - 1 - r] = key[r][c]
#     return n_board


# def solution(key, lock):
#     answer = 'true'
#     n = len(lock)
#     m = len(key)

#     n_lock = [[0] * (n + 2*m) for _ in range(n+2*m)]
#     for i in range(m, n+m):
#         for j in range(m, n+m):
#             n_lock[i][j] = lock[i-m][j-m]
    
#     for i in range(n+m):
#         for j in range(n+m):
#             n_key = key.copy()
#             for _ in range(4):
#                 n_key = rotate(n_key)
#                 print(n_key)
#                 temp_lock = n_lock.copy()

#                 cnt = 0
#                 for r in range(m, m+n):
#                     for c in range(m, m+n):
#                         temp_lock[r][c] += n_key[r-m][c-m]
#                         if temp_lock[r][c] != 0:
#                             cnt +=1
#                 if cnt == n*n:
#                     return True

#     return False

# print(solution([[0,0,0], [1,0,0], [0,1,1]], [[1,1,1], [1,1,0], [1,0,1]]))


def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False