# https://ide.geeksforgeeks.org/RRPgMA8lrI

num = 3     
vals = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
romans=[ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
res=''
        
for i,v in enumerate(vals):
          
    res += (num//v) * romans[i];
    num %= v
            
print(res)

# https://leetcode.com/problems/integer-to-roman/
