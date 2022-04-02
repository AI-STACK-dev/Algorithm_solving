import sys; input = sys.stdin.readline;
s, k, h = map(int, input().split())
MIN = min(s,k,h)
if s + k + h < 100:
    if MIN == s:
        print("Soongsil")
    if MIN == k:
        print("Korea")
    if MIN == h:
        print("Hanyang")
else:
    print("OK")