def common(a,b):
    i=0;la=len(a);lb=len(b)
    while(i<la and i<lb and a[i]==b[i]):
        i+=1
    return a[:i]
   
l=input().strip().split()
s=l[0]
# print(s)
for i in l:
    s=common(s,i)
print(s)
