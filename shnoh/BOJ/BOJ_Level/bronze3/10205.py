import sys; input = sys.stdin.readline;
k = int(input())
for i in range(k):
    b = c = 0
    h = int(input())
    data = input().rstrip()
    for x in data:
        if x == 'b': b += 1
        else: c += 1
    print(f"Data Set {i + 1}:")
    print(h - b + c)
    print()