import sys; input = sys.stdin.readline;
h, m, s = map(int, input().split())
sec = s + 60 * (m + h * 60)
Max = 24 * 60 * 60
q = int(input())
for _ in range(q):
    s = input().rstrip()
    if len(s) == 1:
        temp = sec
        hh = temp // 3600
        temp = temp % 3600
        mm = temp // 60
        ss = temp % 60
        print(hh, mm, ss)
    else:
        x, c = map(int, s.split())
        if x == 2:
            sec -= c
            if sec < 0:
                sec += Max
        else:
            sec += c
            if sec >= Max:
                sec -= Max