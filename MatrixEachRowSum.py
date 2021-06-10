https://ide.geeksforgeeks.org/FACZN6JoaG

mat=[list(map(str,input().split())) for i in range(5)]

res=0;s=''
for i in range(5):
    # res=''
    s+=''.join(mat[i])
    res+=int(s)
    s=''
    
    # 3542+ 245 +45678 +4921 +12 => 54398
print(res) 

