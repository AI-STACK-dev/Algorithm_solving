# sys.stdin.readline를 써온 게 오히려 문제였다. 그냥 input() 쓰면 되는 걸!
cnt = 0
while True:
    try:
        input()
        cnt += 1
    except EOFError:
        break
print(cnt)