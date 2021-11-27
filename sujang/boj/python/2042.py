import sys; input = sys.stdin.readline
import math

n,m,k = map(int,input().rstrip().split())
data = [ int(input().rstrip()) for _ in range(n) ]
cmds = [ list(map(int,input().rstrip().split())) for _ in range(m+k) ]

NUM = 2**(math.ceil(math.log(len(data),2))+1)-1
tree = [0]*(NUM)

# tree 초기화 함수
def init(start,end,idx):
    if start == end:
        tree[idx] = data[start]
    else:
        mid = (start+end)//2
        tree[idx] = init(start,mid,idx*2) + init(mid+1,end,(idx*2)+1)
    return tree[idx]

init(0,len(data)-1,1)
# print(tree)

# 값 출력 함수
def Print(start,end,target,idx):
    if start == end == target:
        return tree[idx]
    mid = (start+end)//2
    if start <= target <= mid:
        return Print(start,mid,target,idx*2)
    else:
        return Print(mid+1,end,target,(idx*2)+1)

# 값 변경 함수
def modify(start,end,target,idx,diff):
    if target < start or target > end:
        return
    tree[idx] += diff
    if start == end:
        return
    mid = (start+end)//2
    modify(start,mid,target,idx*2,diff)
    modify(mid+1,end,target,(idx*2)+1,diff)

# 구간합 구하는 함수
def sum(start,end,idx,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    # start-end 범위가 left-right 범위보다 크다면
    mid = (start+end)//2
    return sum(start,mid,idx*2,left,right)+sum(mid+1,end,(idx*2)+1,left,right)

for a,b,c in cmds:
    # modify
    if a == 1:
        value = Print(0,len(data)-1,b-1,1)
        modify(0,len(data)-1,b-1,1,c-value)
    # print sum
    else:
        print(sum(0,len(data)-1,1,b-1,c-1))