# n no of factors
a=int(input())
temp=a
li=[]
while temp>0:
	if a%temp==0:
		li.append(temp)
	temp=temp-1
print(*li[::-1])
