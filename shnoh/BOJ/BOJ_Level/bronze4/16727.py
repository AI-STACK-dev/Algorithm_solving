import sys; input = sys.stdin.readline;
p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
p = p1 +p2
s = s1 + s2
if p > s:
    print("Persepolis")
elif p < s:
    print("Esteghlal")
else:
    if s1 > p2:
        print("Esteghlal")
    elif s1 < p2:
        print("Persepolis")
    else:
        print("Penalty")