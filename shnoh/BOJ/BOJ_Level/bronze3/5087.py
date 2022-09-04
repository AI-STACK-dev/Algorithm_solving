import sys; input = sys.stdin.readline;
while True:
    Cheryl = Tania = 0
    data = list(input().split())
    if data[0] == '#':
        break
    for card in data:
        if card == 'A':
            Cheryl += 1
        elif card == '*':
            pass
        else:
            if int(card) % 2:
                Cheryl += 1
            else:
                Tania += 1
    if Cheryl > Tania:
        print("Cheryl")
    elif Cheryl < Tania:
        print("Tania")
    else:
        print("Draw")