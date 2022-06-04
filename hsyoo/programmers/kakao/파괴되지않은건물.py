def solution(board, skills):
    n = len(board)
    m = len(board[0])
    prefix_sum = [[0] * (m+1) for _ in range(n+1)]
    # print(n, m, len(prefix_sum)-1, len(prefix_sum[0])-1)
    for skill in skills:
        type, r1, c1, r2, c2, degree = skill
        if type == 1:
            prefix_sum[r1][c1] -= degree
            prefix_sum[r2+1][c1] += degree
            prefix_sum[r1][c2+1] += degree
            prefix_sum[r2+1][c2+1] -= degree
        else:
            prefix_sum[r1][c1] += degree
            prefix_sum[r2+1][c1] -= degree
            prefix_sum[r1][c2+1] -= degree
            prefix_sum[r2+1][c2+1] += degree

    for row in range(n):
        for col in range(m):
            prefix_sum[row][col+1] += prefix_sum[row][col]

    for col in range(m):
        for row in range(n):
            prefix_sum[row+1][col] += prefix_sum[row][col]
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

# def solution(board, skill):
#     answer = 0
#     tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)] # 누적합 기록을 위한 배열
 
#     for type, r1, c1, r2, c2, degree in skill:
#         # 누적합 기록, 부호에 주의할 것
#         tmp[r1][c1] += degree if type == 2 else -degree
#         tmp[r1][c2 + 1] += -degree if type == 2 else degree
#         tmp[r2 + 1][c1] += -degree if type == 2 else degree
#         tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
#     for temp in tmp:
#         print(temp)
#     print()

#     # 행 기준 누적합
#     for i in range(len(tmp) - 1):
#         for j in range(len(tmp[0]) - 1):
#             tmp[i][j + 1] += tmp[i][j]
 
#     # 열 기준 누적합
#     for j in range(len(tmp[0]) - 1):
#         for i in range(len(tmp) - 1):
#             tmp[i + 1][j] += tmp[i][j]
#     for temp in tmp:
#         print(temp)
#     print()
#     # 기존 배열과 합함
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             board[i][j] += tmp[i][j]
#             # board에 값이 1이상인 경우 answer++
#             if board[i][j] > 0: answer += 1
 
#     return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	,[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	 ))
# print(solution([[1,2,3],[4,5,6],[7,8,9]]	, [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	))