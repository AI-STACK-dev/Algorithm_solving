import sys; input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        exit()
    stack = []
    isSuccess = True
    for c in string:
        if c == '[' or  c == '(':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isSuccess = False
                break
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isSuccess = False
                break
    if isSuccess == True and not stack:
        print('yes')
    else:
        print('no')    
