#Your code below
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

