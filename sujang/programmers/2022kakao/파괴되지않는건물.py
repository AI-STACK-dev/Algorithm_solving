'''
문제 6. 40분 / 50점
- 효율성 잡는방식 생각 못함
'''

def solution1(board, skill):
    for typ,lx,ly,rx,ry,deg in skill:
        # 적의 공격 or 아군의 회복
        if typ == 1:
            deg = -deg
        # board 업데이트
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                board[i][j] += deg
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt +=1
    # 최종 결과 리턴
    return cnt

# 효율성 테스트를 위한 수정 코드
def solution(board, skill):
    nx = len(board)
    ny = len(board[0])
    cuSum = [[0]*ny for _ in range(nx)]
    for typ,lx,ly,rx,ry,deg in skill:
        # 적의 공격 or 아군의 회복
        if typ == 1:
            deg = -deg
        # cuSum board 업데이트
        cuSum[lx][ly] += deg
        if rx+1 < nx:
            cuSum[rx+1][ly] -= deg
        if ry+1 < ny:
            cuSum[lx][ry+1] -= deg
        if rx+1 < nx and ry+1 < ny:
            cuSum[rx+1][ry+1] += deg
    # cuSum board 누적합 수행, left -> right
    for i in range(nx):
        for j in range(ny):
            if j != 0:
                cuSum[i][j] += cuSum[i][j-1]
    # cuSum board 누적합 수행, top -> bottom
    for i in range(ny):
        for j in range(nx):
            if j != 0:
                cuSum[j][i] += cuSum[j-1][i]    

    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+cuSum[i][j] > 0:
                cnt +=1
    # 최종 결과 리턴
    return cnt