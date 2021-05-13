# https://ide.geeksforgeeks.org/lWsdd5CYUv
  
n=int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
count = 1
t, b = 0, n-1

while t < b: 
    for i in range(t, b):
        matrix[t][i] = count
        count += 1
    for i in range(t,b):
        matrix[i][b] = count
        count += 1
    for i in range(b,t,-1):
        matrix[b][i] = count
        count += 1
    for i in range(b,t,-1):
        matrix[i][t] = count
        count += 1
    t += 1
    b -= 1
if n % 2 == 1:
    matrix[t][b] = count
        
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print("")
    
    
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

