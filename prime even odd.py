#Your code below
l=list(map(int,input().split()))
l=sorted(l)
x=[];y=[]
for k in range(len(l)):
    for i in range(2,l[k]):
        if(l[k]%i==0):
            flag=0
            break
    else:
      x.append(l[k])
for i in x:
    l.remove(i)
for i in l:
    if i%2==1:
        x.append(i)
        y.append(i)
for i in y:
    l.remove(i)
for i in l:
    if i%2==0:
        x.append(i)
print(*x)