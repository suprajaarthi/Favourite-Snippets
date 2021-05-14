n=int(input())
for i in range(1,n*2):
    for j in range(1,n*2):
        if(i+j==n+1 or i-j==n-1):
            print(i,end=" ")
        elif i+j==(n*3-1):
            print(j+(n-1),end=" ")
        elif j-i==n-1:
            print((n-1)-i+(n*3-1),end=" ")
        else:
            print("*",end=" ")
    print("")



# ip=5
# op:
# * * * * 1 * * * * 
# * * * 2 * 16 * * * 
# * * 3 * * * 15 * * 
# * 4 * * * * * 14 * 
# 5 * * * * * * * 13 
# * 6 * * * * * 12 * 
# * * 7 * * * 11 * * 
# * * * 8 * 10 * * * 
# * * * * 9 * * * * 
