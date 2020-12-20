#no of ways to decode string value

s=input().strip()
if not s or s[0]=='0':
    print("0")
temp=[1]+[0]*len(s)
for i in range(1,len(s)+1):
    if s[i-1]!='0':
        temp[i]+=temp[i-1]
        
    if i>1 and '09'<s[i-2]+s[i-1]<='26':
        temp[i]+=temp[i-2]
        
print(temp[-1])