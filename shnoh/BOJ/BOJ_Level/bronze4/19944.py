import sys; input = sys.stdin.readline;
N, M = map(int, input().split())
if M < 3:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")