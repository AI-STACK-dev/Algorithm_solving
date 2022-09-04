import sys; input = sys.stdin.readline;
while True:
    a, b, c= map(float, input().split())
    np = True
    if a == 0:
        break
    if a <= 4.5 and b >= 150 and c >= 200:
        print("Wide Receiver", end = ' ')
        np = False
    if a <= 6 and b >= 300 and c >= 500:
        print("Lineman", end = ' ')
        np = False
    if a <= 5 and b >= 200 and c >= 300:
        print("Quarterback", end = ' ')
        np = False
    if np:
        print("No positions", end = ' ')
    print()