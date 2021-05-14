# https://ide.geeksforgeeks.org/HX3XHuUwSp
 
n=int(input())
if n < 3: 
    dp = [0, 1, 2]

dp = [0, 1, 2] + [0]* (n )  
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] 
    
print(dp[n])


# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
