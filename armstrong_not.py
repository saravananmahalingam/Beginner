a=input()
s1=0
for i in range(len(a)):
	s1=s1+int(a[i])**len(a)
if a==str(s1):
	print('yes')
else:
	print('no')
