import sys; input = sys.stdin.readline

n = int(input().rstrip())
B = list(map(int,input().rstrip().split()))

tree = [0]*(len(B)*4)
ans = [0]*len(B)

# tree update
def init(start,end,idx):
	# 리프 노드인 경우
	if start == end:
		tree[idx] = 1
	else:
		mid = (start+end)//2
		tree[idx] = init(start,mid,idx*2) + init(mid+1,end,(idx*2)+1)
	return tree[idx]

# segment tree update
def update(start,end,idx,value):
	tree[idx] -= 1
	if start == end:
		return start
	mid = (start+end)//2
	if tree[(idx*2)+1] >= value:
		return update(mid+1,end,(idx*2)+1,value)
	else:
		return update(start,mid,idx*2,value-tree[(idx*2)+1])

init(0,len(B)-1,1)
for i in range(len(B)-1,-1,-1):
	idx = update(0,len(B)-1,1,B[i]+1)
	ans[idx] = i+1
# A 출력
print(*ans)