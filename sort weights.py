#Zoho program 
#Sort weights based on conditions

import math
n=int(input()) ;ki=[]
l=list(map(int,input().split()))
for i in l:
    c=0
    k=math.floor(math.sqrt(i))
    if k*k==i:
        c+=5
    if i%4==0 and i%6==0:
        c+=4
    if i%2==0:
        c+=3
    ki.append([i,c])
ki.sort(key=lambda ki:ki[-1])
for i in ki:
    print(*i)

    
# https://ide.geeksforgeeks.org/BIRzBskGYR
# http://kiruthikamani.blogspot.com/2016/06/sorting-array-with-weight-zoho.html
