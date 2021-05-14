# https://ide.geeksforgeeks.org/0WWRaZHlvg

n=int(input())
l=[list(map(int,input().split())) for i in  range(n)]
l1=sorted(l,key =lambda x:(x[0]))
l2=sorted(l1,key =lambda x:(x[1]))
l3=sorted(l2,key =lambda x:(x[-1]))
print(l3)

# ip: {{20,  1, 2014},
#                   {25,  3, 2010},
#                   { 3, 12, 1676},
#                   {18, 11, 1982},
#                   {19,  4, 2015},
#                   { 9,  7, 2015},
#                     { 18 ,12, 2014},
#                     {1 3 1676}
# };

#  op=>Sorted Dates : 
# [[1, 3, 1676], [3, 12, 1676], [18, 11, 1982], [25, 3, 2010], [20, 1, 2014], 
# [18, 12, 2014]]
