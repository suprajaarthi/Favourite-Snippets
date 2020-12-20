r,c=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(r)]
for i in range(min(c//2,r)):
    for j in range(r-i):
        print(l[j][i],end=" ")
    for j in range(i+1,c-i-1):
        print(l[-1-i][j],end=" ")
    for j in range(r-i-1,-1,-1):
        print(l[j][-1-i],end=" ")
    print()