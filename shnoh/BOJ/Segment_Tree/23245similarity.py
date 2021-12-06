import sys
input = sys.stdin.readline

def cumulative_sum(index, tree): # 처음부터 index까지의 누적합을 계산하는 함수
    Sum = 0 # 누적합을 저장하는 변수
    while index > 0: # tree의 index는 1 ~ N
        Sum += tree[index] # 차례로 더해주면 처음부터 index까지의 누적합
        index -= index & -index # 'index & -index'는 1이 존재하는 최하위 비트를 찾아준다. index에 이것을 빼줘가면, 누적합을 위한 인덱스를 차례로 찾을 수 있다.
    return Sum

def update(index, value, tree): # 해당 위치(index)에 기존 값과의 변화랑 value를 update해 준다. 해당 index가 포함된 구간합들도 update해 준다.
    while index < len(tree): # tree의 index는 1 ~ N
        tree[index] += value # 변화된 값에 따른 구간합 갱신
        index += index & -index # index에 1이 존재하는 최하위 비트를 더해가면, 영향을 끼치는 구간합들의 index들을 탐색할 수 있다.

def solve(q, n, tree, tree_double):
    count = 0
    # last = (p[0] + 1) % 1000000
    # overlap = 0
    # temp = []
    for i in range(n):
        count += cumulative_sum(q[i], tree_double)
        # q[i]까지의 구간합.
        new_pairs = cumulative_sum(q[i], tree)
        last_pairs = cumulative_sum(q[i] + 1, tree_double) - cumulative_sum(q[i], tree_double)
        # overlap = 0
        # if p[i] == last:
        #     for num in temp:
        #         if q[i] > num:
        #             overlap += 1
        #     temp.append(q[i])
        # else:
        #     temp = [q[i]]
        update(q[i] + 1, 1, tree) # tree index는 1부터 위치하므로, 0부터 존재하는 수를 맞추기 위해 + 1
        update(q[i] + 1, cumulative_sum(q[i], tree), tree_double)
        # last = p[i]
    return count
        
tree = [0] * 1000002 # tree : leaf는 나온 위치의 수 0 ~ 10^6 를 1로 조정하는 펜윅트리, 누적합은 q[i]보다 작은 수의 개수.
tree_double = [0] * 1000002 # tree_double : leaf는 현재까지 검사한 q 수열에서 q[i]로 끝나는 2길이 증가쌍의 개수, q[i]보다 작은 누적합은 2길이 증가쌍의 개수 -> 3길이 증가쌍의 개수!

n = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
PQ = []
P = []
Q = []

for i in range(n):
    PQ.append([p[i], -q[i]])
PQ.sort()
for i in range(n):
    P.append(PQ[i][0])
    Q.append(-PQ[i][1]) 

print(solve(Q, n, tree, tree_double))