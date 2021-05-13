n,x=map(int,input().split())
l,m,q,res=[],[],[],[]
for i in range(n):
    a,b=map(str,input().split())
    l.append(a)
    q.append(int(b))
m=sorted(q)
m=m[::-1]
d={};c=1
for i in range(len(m)):
    if(m[i] not in d):
        d[m[i]]=c
        # assign rank as key to mark ( value )
        c+=1
    else:
        c+=1
        
# print(d)
for i in d:
    if d[i]==x:
        res.append(i)
if(res==[]):
    print("-1")
    quit()
k=res[0]
ind,op=[],[]
for i in range(len(m)):
    if(q[i]==k):
        ind.append(i)
for i in ind:
    op.append(l[i])
op=sorted(op)
for i in op:
    print(i)
    
#     https://ide.geeksforgeeks.org/LWQSwof5vv
