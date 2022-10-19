import sys; input = sys.stdin.readline;
h = int(input())
M = int(input())
check = True
for t in range(1, M + 1):
    res = t + 2 * t ** 2 + h * t ** 3 - (6 * t ** 4)
    if res <= 0:
        print(f"The balloon first touches ground at hour: {t}")
        check = False
        break
if check:
    print("The balloon does not touch ground in the given time.")