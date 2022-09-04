import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    data.sort()
    if data[0] + data[1] <= data[2]:
        print(f'Case #{i+1}: invalid!')
    elif data[0] == data[1] and data[1] == data[2]:
        print(f'Case #{i+1}: equilateral')
    elif data[0] == data[1] or data[1] == data[2]:
        print(f'Case #{i+1}: isosceles')
    else:
        print(f'Case #{i+1}: scalene')