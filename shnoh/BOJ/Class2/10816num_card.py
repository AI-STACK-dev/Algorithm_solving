import sys; input = sys.stdin.readline;
from collections import Counter
n = int(input())
data = [int(x) for x in input().split()]
m = int(input())
query = [int(x) for x in input().split()]
#print(data, query)
counter = Counter(data)
for num in query:
    print(counter[num], end = ' ')