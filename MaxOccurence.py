https://ide.geeksforgeeks.org/aeORLn2iOJ

# First Maximum occurence of characters 
s=input().strip()
s=sorted(s)[::-1];op=[]
# print(s)
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
# print(dict)
val=dict.values()
max_val=max(val)
# print(max_val)
for i in dict:
    if dict[i]==max_val:
        op.append(i)
print(str(op[0])+" "+str(max_val))
# print(max_val)

IP : zohoz
OP : z 2
