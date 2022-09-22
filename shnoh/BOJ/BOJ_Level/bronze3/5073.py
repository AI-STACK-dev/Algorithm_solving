import sys; input = sys.stdin.readline;
while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    data.sort()
    n = len(set(data))
    if data[0] + data[1] <= data[2]:
        print("Invalid")
    elif n == 1:
        print("Equilateral")
    elif n == 2:
        print("Isosceles")
    else:
        print("Scalene")