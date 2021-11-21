import sys; input = sys.stdin.readline

string = input().rstrip().split('-')
s = 0
for i in string[0].split('+'):
    s += int(i)

for i in string[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)