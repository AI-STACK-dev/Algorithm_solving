for a in range(6, 101):
    for b in range(2, a - 2):
        for c in range(b + 1, a - 1):
            for d in range(c + 1, a):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")