
#String Inplace swap while rest in same position

n=int(input())
string,x=input().strip(),[]
for i in range(len(string)):
    if (i+1)%n==0:x.append(string[i]) 
for i in range(len(string)):
    if (i+1)%n==0:
        print(x[-1],end='')
        x.pop()
    else:print(string[i],end='')
      
      
      
      
#       https://ide.geeksforgeeks.org/ixohDv39zL
