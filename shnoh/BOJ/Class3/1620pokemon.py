import sys; input = sys.stdin.readline;
# pokedex
num_key = dict()
name_key = dict()
n, m = map(int, input().split())
for i in range(n):
    s = input().rstrip()
    num_key[i + 1] = s
    name_key[s] = i + 1
for _ in range(m):
    s = input().rstrip()
    if ord(s[0]) > 48 and ord(s[0]) <= 57: # 숫자면
        print(num_key[int(s)])
    else:
        print(name_key[s])