import sys; input = sys.stdin.readline;
k, l = map(int, input().split())
good = True
for i in range(2,l):
    if k % i == 0:
        print("BAD", i)
        good = False
        break
if good:
    print("GOOD")