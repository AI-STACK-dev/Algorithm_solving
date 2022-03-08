import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(4)]
res = 0
same = True
for i in range(3):
    if data[i] < data[i + 1]:
        res += 1
        same = False
    elif data[i] > data[i + 1]:
        res -= 1
        same = False
if res == 3:
    print("Fish Rising")
elif res == -3:
    print("Fish Diving")
elif res == 0 and same:
    print("Fish At Constant Depth")
else:
    print("No Fish")