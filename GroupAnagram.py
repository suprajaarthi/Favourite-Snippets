
https://ide.geeksforgeeks.org/hHtFeeTK71
  
l=list(map(str,input().split()))
anag={}

for i in l:
    s=''    
    for j in sorted(i):
        s+=j
        
    if s not in anag:
        anag[s]=[]
        anag[s].append(i)
    else:
        anag[s].append(i)

print(anag)
print(list(anag.values()))
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
