# 입력
n = int(input())
DATA = [list(input()) for _ in range(n)]
Min = (n**2) + 1
P = n//2

for r in range(1 << n):
    num = 0
    data = [DATA[i][:] for i in range(n)]
    for j in range(n):
        count = 0
        for i in range(n):
            if r & (1 << i):
                if data[i][j] == 'H':
                    data[i][j] = 'T'
                else:
                    data[i][j] = 'H'
            if data[i][j] == 'T':
                count += 1
        if count > P:
            count = n - count
        num += count
    Min = min(num,Min)    
print(Min)