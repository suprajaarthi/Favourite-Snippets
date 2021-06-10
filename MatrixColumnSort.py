https://ide.geeksforgeeks.org/49xt8oTYII

r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
k=int(input())
res=sorted(mat,key=lambda row:row[k])
for i in res:
    print(*i)

https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort
    
ip:
  
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

op: 
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
  
