import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(2)]
if data[0] >= 3 and data[1] <= 4:
    print("TroyMartian")
if data[0] <= 6 and data[1] >= 2:
    print("VladSaturnian")
if data[0] <= 2 and data[1] <= 3:
    print("GraemeMercurian")