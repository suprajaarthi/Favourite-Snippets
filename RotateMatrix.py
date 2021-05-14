# https://ide.geeksforgeeks.org/btqq4hCPj0

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
l=[];v=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(arr[n-i-1][j])
    v.append(l)
print(*v)

for i in range(n):
    for j in range(n):
        print(v[j][i],end=" ")
    print("")

ip:
4
1 2 3 4
5 6 7 8
9 10 11 12 
13 14 15 16


op:
[13, 14, 15, 16] [9, 10, 11, 12] [5, 6, 7, 8] [1, 2, 3, 4]
13 9 5 1 
14 10 6 2 
15 11 7 3 
16 12 8 4 
