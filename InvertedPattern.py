    https://ide.geeksforgeeks.org/3eaBhqW0kD

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

IP 5 
OP 

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
15 14 13 12 11 
10 9 8 7 
6 5 4 
3 2 
1 

    
    
    
