# find number of special characters
a=input()
c=0
for i in a:
	if i.isalnum() | i.isspace():
		continue
	else:
		c=c+1
print(c)
