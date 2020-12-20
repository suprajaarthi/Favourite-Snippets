#Your code below
#Generate all possible combinations of word using itertools package
import  itertools 
s=input()
l=[]
n=len(s)
for i in range(1,n+1):
    l.append(list(itertools.combinations(s,i)))
print(*l)
for j in l:
    for k in j:
        print(''.join(k),end=" ")