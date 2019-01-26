N,A,D=map(int,input().split())
c=0
while N:
	c=c+A+(N-1)*D
	N=N-1
print(c)
