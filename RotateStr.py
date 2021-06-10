https://ide.geeksforgeeks.org/1U76Cc6ehz 
  
a="amazon"; b= "azonam" 
# Given two strings, the task is to find if a string can be obtained by rotating another string two places. 

# Examples: 

# Input: string1 = “amazon”, string2 = “azonam” 
# Output: Yes 
# // rotated anti-clockwise
# Input: string1 = “amazon”, string2 = “onamaz” 
# Output: Yes 
# // rotated clockwise
c=b[:2]+b[2:]
d=b[2:]+b[:2]
print(c)
print(d)
