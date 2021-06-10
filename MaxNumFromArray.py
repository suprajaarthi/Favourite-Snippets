https://ide.geeksforgeeks.org/AmuA8il0sy

  
from itertools import permutations
l=[54, 546, 548, 60]

lst = []
for i in permutations(l, len(l)):
     # provides all permutations of the list values,
    # print(i)
    
    # store them in list to find max
    lst.append("".join(map(str,i)))
print(max(lst))
 
# print(largest([54, 546, 548, 60])) #Output 6054854654

