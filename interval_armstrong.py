a,b=map(int,input().split())
for i in range(a,b):
	c=i
	s1=0
	while c>0:
		d=c%10
		s1=s1+d**3
		c=c//10
		if s1==i:
			print(i)
