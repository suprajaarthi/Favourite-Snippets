# https://ide.geeksforgeeks.org/pwScY3UQ3g

#Your code below
# Sort list based on a and a*b
n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b,a*b])
    
print(l)
l=sorted(l,key=lambda l:l[0])
print(l)
l=sorted(l,key=lambda l:l[-1])
# print(l)
for i,j,k in l:
    print(i,j,k,end=" ")
    print("")

    
    
    
