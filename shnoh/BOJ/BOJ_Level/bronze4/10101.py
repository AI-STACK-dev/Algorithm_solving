import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(3)]
if data[0] + data[1] + data[2] != 180:
    print("Error")
elif data[0] == data[1] and data[0] == data[2]:
    print("Equilateral")
elif data[0] == data[1] or data[2] == data[1] or data[0] == data[2]:
    print("Isosceles")
else:
    print("Scalene")
