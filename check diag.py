#Check how many top right bottom diagonals are same

r,c=map(int,input().split(" "))
l=[list(input().split()) for i in range(r)]
n=1-c
Count=0
x=0
while x!=(r+c)-1:
    lis=[]
    for i in range(0,r):
        for j in range(0,c):
            if i-j==n:
                lis.append(l[i][j])
    # print(lis)
    if len(set(lis))==1:
        Count=Count+1
    n=n+1
    x=x+1
print(Count)