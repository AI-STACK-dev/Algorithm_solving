import sys; input =sys.stdin.readline

n,m = map(int,input().rstrip().split())
dict = {}
for i in range(1,n+1):
    name = input().rstrip()
    dict[name] = i
    dict[i] = name
for _ in range(m):
    temp = input().rstrip()
    if temp.isdigit():
        print(dict[int(temp)])
    else:
        print(dict[temp])