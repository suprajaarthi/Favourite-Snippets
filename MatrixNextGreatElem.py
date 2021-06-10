https://ide.geeksforgeeks.org/CFT5hsjFt5
  
 
# Check next great element downwards if large elem is odd replace with it
# or if curr elem is large repl with *

r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    for j in range(c):
        k=mat[i][j]
        
        b=k
        for x in range(i+1,r):
            u=mat[x][j]
            if u>k and u%2==1:
                k=u
        if k==b:
            print("*",end=' ')
        else:
            print(k,end=' ')
    print("")
    
# OP   
# 7 5 9 
# 7 * 9 
# * * * 
