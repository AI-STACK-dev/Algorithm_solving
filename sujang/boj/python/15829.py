n = int(input())
print(sum([(ord(s)-ord('a')+1)*(31**i) for i,s in enumerate(input())])%1234567891)