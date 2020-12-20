
#Use count in key lambda
n=int(input())
l=[]
for i in range(n):
    a=input().split()
    l.append(a[-1])
a=sorted(l,key=l.count,reverse=True)
d=dict()
for i in a:
    if not i in d:
        print(i,a.count(i),sep=" ")
        d[i]=True
