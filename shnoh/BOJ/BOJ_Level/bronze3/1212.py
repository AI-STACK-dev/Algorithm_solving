import sys; input = sys.stdin.readline;
data = bin(int('0o' + input().rstrip(), 8))
data = data[2:]
print(data)