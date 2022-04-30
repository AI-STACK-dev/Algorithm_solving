import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(4)]
tele = True
if data[1] != data[2]:
    tele = False
if data[0] != 8 and data[0] != 9:
    tele = False
if data[3] != 8 and data[3] != 9:
    tele = False
if tele:
    print("ignore")
else:
    print("answer")