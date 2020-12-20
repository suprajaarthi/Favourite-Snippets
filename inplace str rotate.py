#Inplace string rotation

s=input().strip()
s=list(s)
l1=[i for i in s if s.count(i)>1] 
print(l1)
l1=l1[1:]+l1[:1] 
print(l1)
c=0 
for i in s:
    if s.count(i)==1:
        print(i,end='')
    else:
        print(l1[c],end='')
        c+=1