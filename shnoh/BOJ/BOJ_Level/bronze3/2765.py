import sys; input = sys.stdin.readline;
import math
cnt = 0
while True:
    diameter, revolution, sec = map(float, input().split())
    if revolution == 0:
        break
    cnt += 1
    distance = math.pi * diameter * revolution / 63360
    MPH = distance / sec * 3600
    print(f'Trip #{cnt}:{distance: .2f}{MPH: .2f}')