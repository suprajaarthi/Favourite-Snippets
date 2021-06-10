n=int(input())
l,c=[],1
for i in range(n,0,-2):
    k=[]
    for j in range(i):
        k.append(c)
        c+=1
    l.append(k)
    
for i in range((n//2)+1):
    for j in range(i+1):
        print(l[j][0],end=" ")
        l[j]=l[j][1:]
    print("")

for i in range(n//2,0,-1):
    for j in range(i):
        print(l[j][0],end=" ")
        l[j]=l[j][1:]
    print("")

# IP : 7 
  
# OP 

# 1 
# 2 8 
# 3 9 13 
# 4 10 14 16 
# 5 11 15 
# 6 12 
# 7 


