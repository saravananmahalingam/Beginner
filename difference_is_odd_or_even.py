# find difference and checkit is odd or even
a,b=map(int,input().split())
c=abs(a-b)
if c%2==0:
	print("even")
else:
	print("odd")
