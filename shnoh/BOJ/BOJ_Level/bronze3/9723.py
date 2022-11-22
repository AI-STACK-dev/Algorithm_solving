import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    data.sort()
    if data[0] ** 2 +  data[1] ** 2 ==  data[2] ** 2:
        s = "YES"
    else:
        s = "NO"
    print(f"Case #{i + 1}: {s}")