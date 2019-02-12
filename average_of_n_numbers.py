# average of given n numbers
a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
	c=c+i
	d=c//a
print(d)
