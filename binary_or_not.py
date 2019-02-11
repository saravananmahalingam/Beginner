# binary representation
a=int(input())
b=str(a)
c=0
for i in range(len(b)):
	if b[i]!='0' and b[i]!='1':
		c=c+1
if c==0:
	print("yes")
else:
	print("no")
