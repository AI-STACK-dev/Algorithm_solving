# BOJ 14502
import sys; input = sys.stdin.readline;

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
#print(A)
temp = [[0] * m for _ in range(n)] # data를 바꿔가면서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_area = 0

# 안전영역 count. temp를 받아서
def safety_area():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

# virus 전파 바이러스가...
def virus_DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and temp[nx][ny] == 0: # n,m방향이 x,y
            temp[nx][ny] = 2
            virus_DFS(nx, ny)
# 모든 경우의 수 64C3
def solve_DFS(count):
    global max_area

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_DFS(i, j)
        max_area = max(max_area, safety_area())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                solve_DFS(count)
                data[i][j] = 0
                count -= 1
        
solve_DFS(0)
print(max_area)




