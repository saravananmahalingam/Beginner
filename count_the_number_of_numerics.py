#count the number of numerics
a=input()
c=0
for i in a:
	if i.isnumeric():
		c=c+1
print(c)
