import sys; input = sys.stdin.readline
import math

m,n = map(int,input().rstrip().split())
data = [int(input().rstrip()) for _ in range(m)]

MAX = math.inf
N = 2**(math.ceil(math.log2(m))+1)
tree = [0] * N

# 트리 초기화
def init(start,end,idx):
    if start == end:
        tree[idx] = data[start]
    else:
        mid = (start+end)//2
        tree[idx] = min(init(start,mid,idx*2),init(mid+1,end,(idx*2)+1))
    return tree[idx]

init(0,m-1,1)
# print(tree)

# interval min,max 출력
def Print(start,end,idx,left,right):
    if end < left or start > right:
        return  MAX
    if left <= start and right >= end:
        return tree[idx]
    mid = (start+end)//2
    return min(Print(start,mid,idx*2,left,right),Print(mid+1,end,(idx*2)+1,left,right))

for _ in range(n):
    a,b = map(int,input().rstrip().split())
    print(Print(0,m-1,1,a-1,b-1))