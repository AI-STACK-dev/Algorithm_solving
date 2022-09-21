import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
str2int = defaultdict(int)
int2str = defaultdict(str)

for i in range(n):
    name = input().rstrip()
    str2int[name] = str(i+1)
    int2str[str(i+1)] = name

for i in range(m):
    cmd = input().rstrip()
    if cmd.isalpha():
        print(int(str2int[cmd]))
    else:
        print(int2str[cmd])