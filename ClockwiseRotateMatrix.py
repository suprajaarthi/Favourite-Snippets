https://ide.geeksforgeeks.org/knfsQzfInC

#Your code below
n=int(input())
c=int(input())
a=[list(map(int,input().split())) for i in range(n)]
a=[*zip(*a)]
for i in a:
    print(*i)

    
# ip: 
# 3
# 3
# 1 2 3 
# 4 5 6
# 7 8 9 

# op:
# 1 4 7
# 2 5 8
# 3 6 9

