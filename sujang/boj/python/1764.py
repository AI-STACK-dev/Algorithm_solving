import sys; input = sys.stdin.readline

n,m = map(int,input().split())
N = [ input().rstrip() for _ in range(n)]
M = [ input().rstrip() for _ in range(m)]

ans = list(set(N)&set(M))
print(len(ans))
ans.sort()
print(*ans,sep='\n')