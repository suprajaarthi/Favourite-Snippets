https://ide.geeksforgeeks.org/vfTgzXM1TQ
    
    
# Function to remove zeroes
def removeZero(n):
    res = 0
    d = 1
    while (n > 0):
        if (n % 10 != 0):
            res += (n % 10) * d
            d *= 10
 
        n //= 10
    return res
 
def isEqual(a, b):
    if (removeZero(a) +
        removeZero(b) == removeZero(a + b)):
        return True
    return False
 
# Driver code
a = 105
b = 106
if(isEqual(a, b)):
    print("Yes")
else:
    print("No")
 


# Input: a = 101, b = 102 
# Output: YES 
# 101 + 102 = 203. 
# After removing all zeroes from a, b and c, a = 11, b = 12 and c = 23 
# Now check if a + b = c i.e. 11 + 12 = 23 . So print Yes.
