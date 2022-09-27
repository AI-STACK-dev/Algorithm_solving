n = int(input())
m = int(input())
if m > 0:
    avoid = set(list(map(int, input().split())))
    available = set([str(x) for x in range(10) if x not in avoid])
else:
    available = set([str(x) for x in range(10)])

# print(f"available: {available}")
cur = 100
init_value = abs(n - cur)
lb, ub = 500001, 500001
cur = n
while cur >= 0:
    if set(str(cur)).issubset(available):
        # print(f"lb: {cur}")
        lb = len(str(cur)) + abs(n - cur)
        break
    cur -= 1

cur = n
while cur <= 1000000:
    if set(str(cur)).issubset(available):
        # print(f"ub: {cur}")
        ub = len(str(cur)) + abs(n - cur)
        break
    cur += 1
# print(init_value, lb, ub)
answer = min(init_value, lb, ub)
print(answer)