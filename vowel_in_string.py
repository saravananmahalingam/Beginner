a=input()
c=0
l=['a','e','i','o','u','A','E','I','O','U']
if a.isalpha():
	for i in a:
		if i in l:
			c=c+1
	if c!=0:
		print("yes")
	else:
		print("no")
else:
	print("no")
