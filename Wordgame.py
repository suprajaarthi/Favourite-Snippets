#Your code below
n=int(input())
l=[]
for i in range(n):
    l.append(input().strip())
first,last,ans=[],[],[]
for i in l:
    first.append(i[0])
    last.append(i[-1])
    
for i in range(len(first)):
    if first[i] not in last:
        ans.append(l[i])

res=[]
for i in ans:
    for j in l:
        if i[-1]==j[0]:
            ans.append(j)
        else:
            res.append(j)
            
for i in ans:
    print(i)
        
      
# IP: 
#   4
# rag
# nijem
# manager
# lemon


# OP:
#   lemon
# nijem
# manager
# rag

# https://ide.geeksforgeeks.org/LZqAlYDPOO
