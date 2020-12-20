#Rotate boundary elements of the matrix b y x times

r,c,x=map(int,input().split());x%=4
l=[list(map(int,input().split())) for _ in range(r)]
for i in range(min(r,c)//2):
    print(i)
    t=[l[i][i],l[i][-i-1],l[-i-1][-i-1],l[-i-1][i]]
    print(t)
    t=t[-x:]+t[:-x]
    l[i][i]=t[0]
    l[i][-i-1]=t[1]
    l[-i-1][-i-1]=t[2]
    l[-i-1][i]=t[3]
for i in l:
    print(*i)