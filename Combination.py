# Syntax=>
# combinations(iterator, r)

from itertools import combinations
s=input().strip()
u=int(s)%10;c=0
a=[int(i) for i in s]
a=a[:-1]
l=[]
for i in combinations(a,2):
    # print(i)
    if sum(i)==u and i not in l:
        l.append(i)
        l.append(i[::-1])
        c+=1
if l==[] :
    print(-1)
else:
    print(c)
    
    
#     https://ide.geeksforgeeks.org/erW2iIGHYW
