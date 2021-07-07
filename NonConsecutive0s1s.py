https://ide.geeksforgeeks.org/qDtIUkw4Lb
  
# no consecutive 0s and 1s 
def check(s):
    op=[]
    if(s[-1]==s[-2]):
        return False
    for i in range(len(s)-1):
        if s[i]==s[i-1] or s[i]==s[i+1]:
            return False
            exit()
    return True
        
        
a=input().strip()

res=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        b=a[i:j+1]
        # print(b)
        # print(check(b))
        if(check(b)==True):
            res.append(b)
       
# print(res)
final=sorted(res,key=len)
if final==[]:
    print("")
else:
    print(final[-1])
