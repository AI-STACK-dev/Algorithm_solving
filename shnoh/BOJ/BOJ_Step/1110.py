number=int(input())
cnt=1
N=number
while True:
	ten = int(N)//10
	one = int(N)%10
	new = ten + one
	N=str(one) + str(new%10)
	if int(N)==number:
		break;
	else:
		cnt+=1
print(cnt)