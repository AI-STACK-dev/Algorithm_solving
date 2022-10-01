import sys; input = sys.stdin.readline;
A = [[9.23076, 26.7, 1.835],
    [1.84523, 75, 1.348],
    [56.0211, 1.5, 1.05],
    [4.99087, 42.5, 1.81],
    [0.188807, 210, 1.41],
    [15.9803, 3.8, 1.04],
    [0.11193, 254, 1.88]]
T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    res = 0
    for i in range(7):
        res += int(A[i][0] * (abs(A[i][1] - data[i]) ** A[i][2]))
    print(res)