import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
db = defaultdict(str)
for _ in range(n):
    domain, pw = input().rstrip().split()
    db[domain] = pw

for _ in range(m):
    domain = input().rstrip()
    print(db[domain])