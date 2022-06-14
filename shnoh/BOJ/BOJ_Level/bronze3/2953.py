import sys; input = sys.stdin.readline;
data = [list(map(int,input().split())) for _ in range(5)]
who = 0
Max = 0
for i in range(5):
    if Max < sum(data[i]):
        who = i
        Max = sum(data[i])
print(who + 1, Max)