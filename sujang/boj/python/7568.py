n = int(input())
data = [ list(map(int,input().split())) for i in range(n)]

ans = []
for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1]<j[1]:
            rank += 1
    ans.append(rank)
print(*ans)
