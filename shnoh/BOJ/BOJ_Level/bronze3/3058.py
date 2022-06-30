import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    data2 = []
    for num in data:
        if num % 2 == 0:
            data2.append(num)
    data2.sort()
    print(sum(data2), data2[0])