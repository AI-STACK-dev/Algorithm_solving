import sys; input = sys.stdin.readline

ans = []
i = 1
while True:
    l,p,v = map(int,input().rstrip().split())
    if l==0 and p==0 and v==0:
        break
    a = (v//p)*l
    if (v%p) > l:
        a += l
    else:
        a += (v%p)
    ans.append(f"Case {i}: {a}")
    i+=1
print(*ans,sep='\n')