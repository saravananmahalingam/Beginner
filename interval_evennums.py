N,Q=map(int,input().split())
li=[]
for i in range(N+1,Q):
	if(i%2==0):
		li.append(i)
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
