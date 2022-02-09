import sys; input = sys.stdin.readline;
data = [input().rstrip() for _ in range(3)]
for i in range(3):
    if data[i] == "black":
        data[i] = 0
    elif data[i] == "brown":
        data[i] = 1
    elif data[i] == "red":
        data[i] = 2
    elif data[i] == "orange":
        data[i] = 3
    elif data[i] == "yellow":
        data[i] = 4
    elif data[i] == "green":
        data[i] = 5
    elif data[i] == "blue":
        data[i] = 6
    elif data[i] == "violet":
        data[i] = 7
    elif data[i] == "grey":
        data[i] = 8
    elif data[i] == "white":
        data[i] = 9
ans = (10 * data[0] + data[1]) * 10 ** data[2]
print(ans)