import sys; input = sys.stdin.readline;
n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((b, a))
data.sort()
for nums in data:
    print(nums[1], nums[0])
