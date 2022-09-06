import sys; input = sys.stdin.readline;
n = int(input())
for i in range(n):
    data = input().rstrip()
    tf = []
    for k in data:
        if ord(k) < 97:
            tf.append(chr(ord(k) + 32))
        else:
            tf.append(k)
    print(''.join(tf))