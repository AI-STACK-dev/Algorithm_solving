import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(2)]
res = data[1] - data[0]
if res <= 0:
    print("Congratulations, you are within the speed limit!")
elif res <= 20:
    print("You are speeding and your fine is $100.")
elif res <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")