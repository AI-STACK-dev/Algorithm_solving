import sys; input = sys.stdin.readline;
q = int(input())
data = [input().rstrip() for _ in range(q)]
r = int(input())
for _ in range(r):
    x = int(input())
    if x > 0 and x <= len(data):
        print(f'Rule {x}: {data[x - 1]}')
    else:
        print(f'Rule {x}: No such rule')