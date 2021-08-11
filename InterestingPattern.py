s=input().strip()
t=input().strip()
s=s.replace(':','')
t=t.replace(':','')

c=0

s=int(s);t=int(t)
for i in range(s,t):
    # print(i)
    
    a=str(i)
    b=a[2:4]
    d=a[4:6]
    
    # print(b,d)
    
    if len(set(a))==2 and int(b)<=59 and int(d)<=59 and len(a)!=2:
        print(a)
        c+=1
        
print(c)
