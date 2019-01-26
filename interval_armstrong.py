a,b=map(int,input().split())
x=[]
for i in range(a,b):
	c=i
	s1=0
	e=len(str(i))
	while c>0:
		d=c%10
		s1=s1+d**e
		c=c//10
	if s1==i:
		x.append(i)
print(" ".join(map(str,x)))
