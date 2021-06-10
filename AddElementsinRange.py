https://ide.geeksforgeeks.org/kYdQE5sLwq

lst=list(map(int,input().split()))
ln = len(lst)
res=[]
if (ln % 2) == 0:
    for i in range(0,len(lst),2):
        res.append(sum(lst[i:i+2]))
#         [i:i+2]
#         [0:2]=>[1,2]
#         [2:4]=>[4,7]
          
    print(res)
else:
    print("bad match")

# IP : 1 2 4 7  
# OP : [3, 11]
    

 
