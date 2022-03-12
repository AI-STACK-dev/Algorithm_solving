n = int(input())
if n%10 != 0:
    print(-1)
else:
    values = [300,60,10]
    ans = []
    for v in values:
        cnt = n//v
        ans.append(cnt)
        n -= cnt*v
    print(*ans)
    