# https://ide.geeksforgeeks.org/7FpgI8dvRl
n=535;rev=0;r=0
while n>0:
    # TODO: write code...
    r=n%10
    rev=(rev*10)+r
    n//=10
    
print(rev)
    
# Check if a number is palindrome w/o using arrays or strings
