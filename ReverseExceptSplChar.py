# https://ide.geeksforgeeks.org/zw9dO49yTK

strSample='abc/defgh$ij'
  
#convert string into list
listSample=list(strSample)
  
i=0
j=len(listSample)-1
  
while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        #swap the element in the list 
        #if both elements are alphabets
        listSample[i], listSample[j]=listSample[j], listSample[i]
        i+=1
        j-=1
  
#convert list into string 
#by concatinating each element in the list
strOut=''.join(listSample)
print(strOut)

# Input string: a!!!b.c.d,e'f,ghi
# Output string: i!!!h.g.f,e'd,cba
