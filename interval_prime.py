a,b=map(int,input().split())
li=[]
for i in range(a+1,b):
	c=0
	for j in range(2,i):
		if i%j==0:
			c=c+1
	if c==0:
		li.append(i)
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
