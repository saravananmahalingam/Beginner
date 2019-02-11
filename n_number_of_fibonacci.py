a=int(input())
t1=0
t2=1
li=[]
for i in range(1,a):
	t=t1+t2
	t1=t2
	t2=t
	li.append(t)
print('1',*li)
