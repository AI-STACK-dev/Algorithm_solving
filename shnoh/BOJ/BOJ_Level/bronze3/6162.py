import sys; input = sys.stdin.readline;
k = int(input())
for i in range(k):
    print(f'Data Set {i + 1}:')
    e, a = map(int, input().split())
    x = e / a
    if x <= 1: print("no drought")
    else:
        s = ""
        while x > 5:
            s += "mega "
            x = x / 5
        print(s, "drought", sep = "")
    print("")