import sys; input = sys.stdin.readline
from bisect import bisect_left

n = int(input().rstrip())
data = list(map(int,input().rstrip().split()))

# 1 단계: 정렬 nlogn
sorted_data = sorted(data)
final_data = [sorted_data[0]]
for i in range(1,n):
    if final_data[-1] != sorted_data[i]:
        final_data.append(sorted_data[i])

# 2 단계: bisect 출력
for d in data:
    print(bisect_left(final_data,d), end=' ')
    