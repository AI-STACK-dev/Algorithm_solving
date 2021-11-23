import sys
type_B = list('BWBWBWBW')
type_W = list('WBWBWBWB')
B_board = [type_W if i % 2 else type_B for i in range(8)] #B로 시작하는 체스판
W_board = [type_B if i % 2 else type_W for i in range(8)] #W로 시작하는 체스판

def repaint(I,J): # 리스트에서 8*8만큼 순회: 2개 version의 체스판과 비교하며 최소 변경값 return
    count_B = 0
    count_W = 0
    for i in range(8):
        for j in range(8):
            if data[I + i][J + j] != B_board[i][j]:
                count_B +=1
            if data[I + i][J + j] != W_board[i][j]:
                count_W +=1
    return min(count_B, count_W)
            
n, m = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)] # 입력
res = [[0]*(m - 7) for _ in range(n - 7)] # i행 j열에서 시작하는 8*8체스판을 만들었을 때, 최소 변경값
for i in range(n - 7):
    for j in range(m - 7):
        res[i][j] = repaint(i,j)
print(min(map(min, res))) # 2차원 리스트 최소값