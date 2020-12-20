#Your code below
#Inverted triangle pattern 
a,b=map(str,input().split())
a=int(a);k=a
l=[];d=[];g=[]
for i in range(1,a+1):
    d=[]
    for j in range(1,a-i+2):
        if j==k:
            d.append(j)
            k-=1
        else:
            d.append(j)
            d.append(b)
    g.append(d)
for i in range(len(g)):
    if i%2==0:
        print(" "*i,end="")
        print(*g[i])
    else:
        print(" "*i,end="")
        print(*g[i][::-1])