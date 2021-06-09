# https://ide.geeksforgeeks.org/rkntg0kugB

from itertools import combinations

l=list(map(int,input().split()))
a=combinations(l,2)
print(list(a))

# OP : [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
