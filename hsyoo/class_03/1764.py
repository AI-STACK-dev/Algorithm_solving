import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
listen = set()
unseen = set()
for _ in range(n):
    listen.add(input().rstrip())
for _ in range(m):
    unseen.add(input().rstrip())
answer = list(listen.intersection(unseen))
answer.sort()
print(len(answer))
for item in answer:
    print(item)