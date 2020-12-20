#Inverted U shaped matrix layer wise

m,n=map(int,input().split()) 
l=[input().split() for i in range(m)] 
a,b=0,n-1 
while a<b and a<m:
    for i in range(m-1,a,-1):
        print(l[i][a],end=" ") 
    for i in range(a,b):
        print(l[a][i],end=" ") 
    for i in range(a,m):
        print(l[i][b],end=" ") 
    a,b=a+1,b-1 
    print()
