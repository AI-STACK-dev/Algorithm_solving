import sys; input = sys.stdin.readline;
N = int(input())
# 결국. 해당 수에서 -1. 첫 수는 1. 아닌가??
res = 1
for i in range(N):
    res += int(input()) - 1
print(res)