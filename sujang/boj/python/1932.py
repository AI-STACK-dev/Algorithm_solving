from sys import stdin

n = int(stdin.readline().rstrip())
data = [ list(map(int,stdin.readline().rstrip().split())) for _ in range(n) ]

i=0
for j in range(n):
    if i ==0:
        i+=1
        continue
    else:
        for jj in range(j+1):
            if jj ==0:
                data[i][jj] += data[i-1][jj]
            elif jj == j:
                data[i][jj] += data[i-1][jj-1]
            else:
                data[i][jj] += max(data[i-1][jj-1],data[i-1][jj])
    i+=1

ans = 0
for i in range(n):
    if data[n-1][i] > ans:
        ans = data[n-1][i]
print(ans)