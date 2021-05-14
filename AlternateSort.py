# https://ide.geeksforgeeks.org/9yZ01BcmF6

l=list(map(int,input().split()))
n=len(l)
l=sorted(l)
i=0
j=n-1
while(i<j):
    print(l[j],end=" ")
    print(l[i],end=" ")
    j-=1
    i+=1
if n%2!=0:
    print(l[i])
    
#   ip:6 5 1 7 8 4 2 
#   op:8 1 7 2 6 4 5
