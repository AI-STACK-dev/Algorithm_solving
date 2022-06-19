import sys; input = sys.stdin.readline;
from collections import Counter
data = [list(map(int, input().split())) for _ in range(3)]
raw = list(zip(*data))
x = raw[0]
y = raw[1]
print(Counter(x).most_common(2)[1][0], Counter(y).most_common(2)[1][0])