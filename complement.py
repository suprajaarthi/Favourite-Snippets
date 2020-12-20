
#Complement binary value 

N=int(input())
binval =  bin(N)[2:]
new = ""
for i in range(0,len(binval)):
    if binval[i] =="0":
        new +="1"
    else:
        new+="0"
print(int(new,2))