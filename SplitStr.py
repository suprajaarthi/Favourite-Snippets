s=input().strip()
maxs=0
for i in range(1,len(s)):
    lef=s[:i]
    rig=s[i:len(s)]
    # print(lef)
    # print(rig)
    temp=lef.count('0')+rig.count('1')
    if temp>maxs:
        maxs=temp
print(maxs)

# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
