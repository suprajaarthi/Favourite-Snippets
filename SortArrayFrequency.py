# https://ide.geeksforgeeks.org/sbfxuiX1jI
  
l=list(map(int,input().split()))
print(sorted(l,key=l.count,reverse=True))


# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
