# print odd digits in given number
a=int(input())
li=[]
for i in str(a):
	if int(i)%2!=0:
		li.append(i)
print(*li)
