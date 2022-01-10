import sys; input = sys.stdin.readline;
from collections import Counter
data = list(map(int, input().split()))
S = set(data)
n = len(S)
C = Counter(data)
if n == 1: 
    print(10000 +data[0] * 1000)
elif n == 2:
    print(1000 + C.most_common(1)[0][0] * 100)
else:
    print(max(data) * 100)