#Your code below
#Check values a and b are present in matrix diagonals
r,c=map(int,input().split())
l=[list(map(int,input().split())) for i in range(r)]
a,b=map(int,input().split())
s=[]
for k in range(r+c-1):
    m=[]
    for i in range(r):
        for j in range(c):
            if i+j==k:
                m.append(l[i][j])
    s.append(m)
    

for i in s:
    if a in i and b in i:
        print("YES")
        quit()
n=1-c  

op=[];x=0;res=[]
while x!=(r+c)-1:
    for i in range(0,r):
        for j in range(0,c):
            if i-j==n:
                op.append(l[i][j])
            
    n=n+1
    x=x+1  
    res.append(op)
    op=[]
for i in res:
    if a in i and b in i:
        
        print("YES")
        quit()
        

print("NO")
    



