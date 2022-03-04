n,m = map(int,input().split())
hap = n+m
cha = n-m
if hap<0 or cha<0 or hap%2!=0:
    print(-1)
else:
    print(*sorted([hap//2,cha//2],reverse=True))
