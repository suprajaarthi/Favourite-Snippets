n=int(input())
dic={}
s,d=[],[]
for i in range(n):
    source,dest=input().split()
    d.append(dest)
    s.append(source)
    dic[source]=dest
for i in s:
    if i not in d:
        start=i
        break
for i in range(n):
    print(start+" to "+dic[start])
    start=dic[start]
    
# https://ide.geeksforgeeks.org/lPyc0uDJS2
