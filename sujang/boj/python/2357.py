import sys; input = sys.stdin.readline
import math

m,n = map(int,input().rstrip().split())
data = [int(input().rstrip()) for _ in range(m)]

MAX = math.inf
N = 2**(math.ceil(math.log2(m))+1)
tree = [[0,0] for _ in range(N)]

# 트리 초기화
def init(start,end,idx):
    if start == end:
        tree[idx][0] = data[start]
        tree[idx][1] = data[start]
    else:
        mid = (start+end)//2
        a,b = init(start,mid,idx*2)
        c,d = init(mid+1,end,(idx*2)+1)
        tree[idx][0] = min(a,c)
        tree[idx][1] = max(b,d)
    return tree[idx]

init(0,m-1,1)
# print(tree)

# interval min,max 출력
def Print(start,end,idx,left,right):
    if end < left or start > right:
        return  [MAX,0]
    if left <= start and right >= end:
        return tree[idx]
    mid = (start+end)//2
    a,b = Print(start,mid,idx*2,left,right)
    c,d = Print(mid+1,end,(idx*2)+1,left,right)
    return [ min(a,c) , max(b,d)]

for _ in range(n):
    a,b = map(int,input().rstrip().split())
    print(*Print(0,m-1,1,a-1,b-1))