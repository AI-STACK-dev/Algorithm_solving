import sys; input = sys.stdin.readline;
n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    print(f'Scenario #{i+1}:')
    if data[0] ** 2 + data[1] ** 2 == data[2] ** 2:
        print("yes")
    else:
        print("no")
    print()