https://ide.geeksforgeeks.org/etcum3PBQh
    
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
# print(*l)
leftoryt=True
for i in range(n-1,-1,-1):
    if leftoryt:
        print(*l[i])
    else:
        print(*l[i][::-1])
    leftoryt=not leftoryt

IP 

3
1 2 3
4 5 6 
7 8 9 


OP 

7 8 9
6 5 4
1 2 3



