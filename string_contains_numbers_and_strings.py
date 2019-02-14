# contains both alphabets and numbers
a=input()
c=0
t=0
for i in a:
	if i.isalpha():
		c=c+1
	elif i.isdigit():
		t=t+1
if c>0 and t>0:
	print("yes")
else:
	print("no")
