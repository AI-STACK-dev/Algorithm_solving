n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]
        if j == i:
            right_up = 0
        else:
            right_up = d[i-1][j]
        d[i][j] = d[i][j] + max(left_up, right_up)
print(max(d[n-1]))