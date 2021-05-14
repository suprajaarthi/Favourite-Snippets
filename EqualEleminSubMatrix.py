n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
k=int(input())
for i in range(0,n,k):
    for j in range(0,n,k):
        p=l[i][j]
        # print(p)
        for a in range(i,i+k):
            for b in range(j,j+k):
                if l[a][b]!=p:
                    print("no")
                    exit()
print("yes")

# Check if all the elements in a k*k matrix are equal
# ip:
# 4
# 10 10 20 20
# 10 10 20 20
# 25 25 30 30
# 25 25 30 30
# k=>2
# op:
#   Yes
