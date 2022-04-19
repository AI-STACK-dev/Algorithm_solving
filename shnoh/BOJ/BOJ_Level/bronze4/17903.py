import sys; input = sys.stdin.readline;
m, n = map(int, input().split())
# data = [ list(map(int, input().split())) for _ in range(m)]
# res = False
# for i in range(m):
#     temp = True
#     for j in range(n):
#         if data[i][j] < 0:
#             temp = False
#     if temp:
#         res = True
#         break
# if res and m >= 8:
#     print("satisfactory")
# else:
#     print("unsatisfactory")
if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")