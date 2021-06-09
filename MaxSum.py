
l=list(map(int,input().split()))
maxsum=l[0];curr=l[0]
for i in l[1:]:
    curr=max(i,curr+i)
    maxsum=max(curr,maxsum)
print(maxsum) 



# IP : -2 1 -3 4 -1 2 1 -5 4 
# EXPLANATION : 4 -1 2 1 => 6
# OP : 6

# https://ide.geeksforgeeks.org/sBYbm5bGlC
