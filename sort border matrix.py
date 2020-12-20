Sort Border Elements in matrix and insert them in matrix

n,k=map(int,input().split())
a=[[int(j) for j in input().split()] for i in range(0,n)]
b=[]
for i in range(n):
    for j in range(k):
        if(i==0 or j==0 or i==n-1 or j==k-1):
            b.append(a[i][j])
b.sort()
# print(b)
# print(len(b))
x=0
for i in range(n):
    for j in range(k):
        if(i==0):
            a[i][j]=b[x]
            x+=1
for i in range(n):
    for j in range(k):
        if(j==k-1 and i!=0):
            a[i][j]=b[x]
            x+=1
x=len(b)-1
# print(x)
for i in range(n):
    for j in range(k):
        if(i!=0 and j==0):
            a[i][j]=b[x]
            x-=1
for i in range(n):
    for j in range(k):
        if(i==n-1 and j!=0):
            a[i][j]=b[x]
            x-=1
for i in range(n):
    for j in range(k):
        print(a[i][j],end=" ")
    print()