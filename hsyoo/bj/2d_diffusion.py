import copy
n,m = map(int, input().split())
ary = []
for i in range(n):
    ary.append(list(map(int, input().split())))
t = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for _ in range(t):
    result = copy.deepcopy(ary)
    for i in range(n):
        for j in range(m):
            for idx in range(4):
                if i + dy[idx] < 0:
                    continue
                elif i + dy[idx] > (n-1):
                    continue
                elif j + dx[idx] < 0:
                    continue
                elif j + dx[idx] > (m-1):
                    continue
                else:
                    result[i][j] += ary[i+dy[idx]][j+dx[idx]]
    ary = copy.deepcopy(result)
print(ary)
