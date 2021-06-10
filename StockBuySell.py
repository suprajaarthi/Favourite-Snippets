https://ide.geeksforgeeks.org/Gj9JOl7ity
  
prices=[7,1,5,3,6,4]
max_num, max_profit = 0, 0
for p in reversed(prices):

    max_profit = max(max_profit, max_num-p)
    max_num = max(max_num, p)

print(max_profit)

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), \
# profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
 
  
  
