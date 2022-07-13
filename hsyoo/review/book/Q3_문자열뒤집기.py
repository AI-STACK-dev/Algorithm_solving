s = input()
while '00' in s:
    s = s.replace('00', '0')
while '11' in s:
    s = s.replace('11', '1')

print(min(s.count('0'), s.count('1')))