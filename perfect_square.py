# perfect square
a,b=map(int,input().split())
c=a*b
d=c**0.5
if d**2 == c:
	print("yes")
else:
	print("no")
