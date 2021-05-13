n=int(input())
dest=[list(map(str,input().split())) for i in range(n)]
on=[];tw=[]
cone=[i[0] for i in dest]
ctwo=[i[1] for i in dest]
for i in ctwo:
    if i not in cone:
        print(i)


# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
