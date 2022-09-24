s=input()
rev=s[::-1]
n=len(rev)
count=0
for i in range(n):
    count=count+1
    if (rev[i]==' '):
        break
res=count-1
print(res)
