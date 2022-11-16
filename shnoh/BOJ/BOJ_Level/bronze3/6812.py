import sys; input = sys.stdin.readline;
t = int(input())
data = ["Ottawa", "Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax","St. John's"]
data2 = [0, -300, -200, -100, 0, 100, 130]
for i in range(7):
    if i == 6 and (t  % 100) >= 30:
        t += 40
    x = (t + data2[i] + 2400) % 2400
    print(f"{x} in {data[i]}")