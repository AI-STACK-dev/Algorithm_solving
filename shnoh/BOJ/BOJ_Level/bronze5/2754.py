import sys; input = sys.stdin.readline;
data = input().rstrip()
if data == 'F':
    print(0.0)
else:
    score = 69 - ord(data[0])
    if data[1] == '+':
        score += 0.3
    elif data[1] == '-':
        score -= 0.3
    print(f'{score:.1f}')