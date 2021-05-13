n=int(input())

for x in range(0,n):
    for y in range(0,x+1):
        print("*",end='')
    print("")
    
for x in range(1,n):
    for y in range(x,n):
        print("*",end='')
    print("")

    
#     Input n= 5 
#     Output : 



*
**
***
****
*****
****
***
**
*

