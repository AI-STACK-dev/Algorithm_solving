import sys; input=sys.stdin.readline
n = int(input().rstrip())
print(*[(' '*(n-i))+('*'*i) for i in range(1,n+1)],sep='\n')