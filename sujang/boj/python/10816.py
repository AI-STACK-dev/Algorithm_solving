from bisect import bisect_left,bisect_right
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
# nlogn
n_list.sort()
# mlogn
for i in range(m):
    target = m_list[i]
    m_list[i] = bisect_right(n_list,target) - bisect_left(n_list,target)
print(*m_list)