https://ide.geeksforgeeks.org/aekdGyPch2
    
    
from itertools import permutations 
a = "GeEK"

p = permutations(a) 
for j in list(p): 
    print(j) 
    
# ('G', 'E', 'K')
# ('G', 'K', 'E')
# ('E', 'G', 'K')
# ('E', 'K', 'G')
# ('K', 'G', 'E')
# ('K', 'E', 'G')
