n = int(input())
ary = []
for i in range(n):
    name, score = input().split()
    ary.append((name, int(score)))

a = sorted(ary, key = lambda x : x[1])
for i in a:
    print(i[0], end = ' ')
