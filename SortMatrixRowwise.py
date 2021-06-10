# https://ide.geeksforgeeks.org/2JAYccCKMH
m,n=map(int,input().split())
l,a=[],[]
for i in range(m):
    l=list(map(int,input().split()))
    l=sorted(l)
    a.append(l)
    
# print(a)
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
    
ip:

3 3

6 1 3
11 9 5 
12 9 1

op:
    
1 3 6 
5 9 11 
1 9 12 

