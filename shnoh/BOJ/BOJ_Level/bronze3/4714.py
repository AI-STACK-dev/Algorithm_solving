import sys; input = sys.stdin.readline;
while True:
    x = float(input())
    if x < 0:
        break
    print(f'Objects weighing {x:.2f} on Earth will weigh {x*0.167:.2f} on the moon.')