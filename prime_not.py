a=int(input())
c=0
if a<1000:
	for i in range(2,a):
		if a%i==0:
			c=c+1
	if c==0:
		print("yes")
	else:
		print("no")
else:
	print("no")
