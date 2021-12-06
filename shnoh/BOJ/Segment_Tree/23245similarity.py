import sys
import itertools
input = sys.stdin.readline


def solve(p, q):
    print(p,q)
    # count = 0
    # triple_p =list(itertools.combinations((p),3))
    # print(triple_p)
    # triple_q =list(itertools.combinations((q),3))
    # set_triple_q = set(triple_q)
    # for x in triple_p:
    #     if x in set_triple_q:
    #         count += 1
    # print(count)

n = int(input())
p = [[int(x)] for x in input().split()]
q = [int(x) for x in input().split()]
p_sort_index = [0] * n
q_sort_index = [0] * n

for i in range(n):
    p[i].append(i)
p.sort()
for i in range(n):
    p_sort_index[i] = p[i][0]
    q_sort_index[i] = q[p[i][1]]

solve(p_sort_index, q_sort_index)

# 조합으로 풀기
# 각각 오름차순으로 정렬해서 인덱스만 남김.
# def solve(p, q):
#     print(p,q)
#     count = 0
#     triple_p =list(itertools.combinations((p),3))
#     print(triple_p)
#     triple_q =list(itertools.combinations((q),3))
#     set_triple_q = set(triple_q)
#     for x in triple_p:
#         if x in set_triple_q:
#             count += 1
#     print(count)

# n = int(input())
# p = [[int(x)] for x in input().split()]
# q = [[int(x)] for x in input().split()]
# p_sort_index = [0] * n
# q_sort_index = [0] * n

# for i in range(n):
#     p[i].append(i)
#     q[i].append(i)
# p.sort()
# q.sort()
# for i in range(n):
#     p_sort_index[i] = p[i][1]
#     q_sort_index[i] = q[i][1]

# solve(p_sort_index, q_sort_index)
