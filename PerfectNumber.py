n=int(input())
l=2;c=1
while(c<n):
    if n%l==0:
        c=c+l
        l=l+1
    else:
        l=l+1
print(c==n)

# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
# For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.


# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
