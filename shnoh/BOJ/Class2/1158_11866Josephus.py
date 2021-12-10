import sys; input = sys.stdin.readline;

n, k = map(int, input().split())
data = [i for i in range(1, n + 1)]
res = []
cur_pointer = 0
cur_n = n 
for _ in range(n):
    cur_pointer = (cur_pointer + k - 1) % cur_n
    res.append(data.pop(cur_pointer))
    cur_n -= 1

print('<', end = '')
for i in range(n - 1):
    print(f'{res[i]},', end = ' ')
print(f'{res[n - 1]}>')