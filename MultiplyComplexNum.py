
a,b=map(str,input().split(','))
ar,ai=a.split('+')
ai=ai[:-1]
br,bi=a.split('+')
bi=bi[:-1]
# print(ar,ai)
# print(br,bi)
resre=(int(ar)*int(br))+(-int(ai)*int(bi))
resim=(int(ar)*int(bi))+(int(br)*int(ai))
print(str(resre)+'+'+str(resim)+'i')


# https://ide.geeksforgeeks.org/pn7RUitRRi

# Example 1:

# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:

# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
  
  
  <img src="https://www.mathsisfun.com/algebra/images/foil-complex.svg">
  
  
