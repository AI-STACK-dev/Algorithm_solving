import math

n = int(input())
m = int(input())
ans = []
for i in range(n,m+1):
    if i == 1:
        continue
    flag = True
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            flag = False
            break
    if flag:
        ans.append(i)

if len(ans):
    print(sum(ans))
    print(min(ans))
else:
    print(-1)
    