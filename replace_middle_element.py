a=input()
l=list(a)
if len(a)%2==1:
	i=len(a)//2
	l[i]="*"
else:
	i=len(a)//2
	l[i]="*"
	l[i-1]="*"
ans=""
for i in l:
	ans+=i
print(ans)
