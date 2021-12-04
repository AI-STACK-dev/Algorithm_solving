import sys;input=sys.stdin.readline
import math

n = int(input())
p = list(map(int,input().rstrip().split()))
q = list(map(int,input().rstrip().split()))

combine = list(zip(p,q))
combine = sorted(combine,key=lambda x: (x[0],-x[1]))

MAX = 1000000+2
stree = [0]*MAX
btree = [0]*MAX

def Sum(idx,tree):
	rtn = 0
	while idx > 0:
		rtn += tree[idx]
		idx -= (idx & -idx)
	return rtn

def change(idx,tree):
	while idx < MAX:
		tree[idx] += 1
		idx += (idx & -idx)

result = [[0,0] for _ in range(n)]
for i in range(n):
    a,b = combine[i][1],combine[n-i-1][1]
    change(a+1,stree)
    change(b+1,btree)
    result[i][0] = Sum(a,stree)
    result[n-i-1][1] = Sum(MAX-1,btree)-Sum(b+1,btree)

ans = 0
for i in range(n):
    a,b = result[i]
    ans += a*b
print(ans)