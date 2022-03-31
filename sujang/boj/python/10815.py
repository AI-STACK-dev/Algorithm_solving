import sys;input=sys.stdin.readline

n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

def binary_search(value):
    first, last = 0, len(nlist)-1
    while first <= last:
        mid = (first + last) // 2
        if nlist[mid] == value:
            return 1
        if nlist[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
    return 0

ans = []
for i in mlist:
    ans.append(binary_search(i))

print(*ans, sep=' ')
