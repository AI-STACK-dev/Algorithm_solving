# import sys; input = sys.stdin.readline;
# n, w, d, Sum = map(int, input().split())
# print(((n * (n - 1) * w // 2) - Sum) // d)

# import sys;
# lines = sys.stdin.readlines()
# for line in lines:
#     n, w, d, Sum = map(int, line.split())
#     print(((n * (n - 1) * w // 2) - Sum) // d)
import sys; input = sys.stdin.readline;
while True:
    try:
        n, w, d, Sum = map(int, input().split())
        k = ((n * (n - 1) * w // 2) - Sum) // d
        if not k:
            k = n
        print(k)
    except:
        break