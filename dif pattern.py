#Your code below
#Pattern using / and \
n=int(input())
for i in range(n):
    for j in range(n):
        if (j == i or j == n - 1 - i): 

        # Condition to print 
        # forword slash 
            if (i == n - 1 - j): 
                print("/",end="") 
  
        # Condition to print 
        # backward slash 
            else: 
                print("\\",end="") 
            
        else:
            print("*",end="")
    print("")