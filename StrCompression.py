s=input().strip()
c=1
res=[]
for i in range(1,len(s)+1):
    if i==len(s):
        print(s[i-1]+str(c),end="")
    elif s[i]==s[i-1]:
        c+=1
    else:
        print(s[i-1]+str(c),end="")
        c=1
    
    
# https://ide.geeksforgeeks.org/BCWd5PMlM9
