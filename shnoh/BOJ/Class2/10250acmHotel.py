import sys
input = sys.stdin.readline

def solve(H,W,N):
    room = 1
    floor = 0
    for _ in range(N):
        floor += 1
        if floor > H:
            room += 1
            floor = 1
    print(floor * 100 + room)

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    solve(h,w,n)