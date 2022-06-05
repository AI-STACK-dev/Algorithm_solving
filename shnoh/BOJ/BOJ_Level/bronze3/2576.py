import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(7)]
Sum = 0
Min = 100
for num in data:
    if num % 2:
        Sum += num
        Min = min(Min, num)
if Sum:
    print(Sum)
    print(Min)
else:
    print(-1)