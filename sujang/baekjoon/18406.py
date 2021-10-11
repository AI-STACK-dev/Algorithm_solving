from sys import stdin

n = [int(num) for num in stdin.readline()[:-1]]
half = len(n)//2
front = sum(n[:half])
back = sum(n[half:])
if front == back:
    print("LUCKY")
else:
    print("READY")