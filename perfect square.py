#Find valid perfect square using BST

num=int(input())
l,h=0,num
while(l<=h):
    m=(l+h)//2
    print(str(l)+" "+str(h))
    if (m*m ==num):
        print("True")
        quit()
    elif (m*m < num):
        l=m+1
    else:
        h=m-1
print("False")