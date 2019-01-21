n=int(input())
m=0
li=[]
for i in range(1,6):
	m=n*i
	li.append(m)
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
