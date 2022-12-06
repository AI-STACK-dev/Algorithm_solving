import sys; input = sys.stdin.readline;
n = int(input())
data = [int(input()) for _ in range(n)]
if sum(data) < n / 2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")