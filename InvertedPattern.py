a=int(input())
k=1
for i in range(1,a+1):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print("")
k-=1
for i in range(a,0,-1):
    for j in range(i):
	    print(k,end=' ')
	    k-=1
    print("")
    
    
    
#     https://ide.geeksforgeeks.org/3eaBhqW0kD
