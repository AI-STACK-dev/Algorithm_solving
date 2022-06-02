import sys; input = sys.stdin.readline;
from collections import Counter
N = int(input())
Max = 0
for _ in range(N):
    counter = Counter(list(map(int, input().split())))
    data = counter.most_common()
    # print(data[0][0])
    if len(data) == 3:
        max_num = max(data[0][0], data[1][0], data[2][0])
        Max = max(Max, max_num * 100)
    else:
        max_num = data[0][0]
        power = data[0][1]
        Max = max(Max, max_num * 10 ** power + 10 ** (power + 1))
print(Max)