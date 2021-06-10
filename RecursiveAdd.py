

n=int(input())
l=list(map(int,input().split()))
a=float('inf')
k=[]
while(len(l)>1):
    k=[]
    for i in range(len(l)-1):
        k.append(l[i]+l[i+1])
    # print(k)
    l=k
    
for i in l: 
    l=str(i)
print(l)
while len(l)>1:
    s=0
    for i in l:
        s+=int(i)
    l=str(s)
    
print(l)

# Explanation 
Input: 5 1 2 3 4 5
Output: 3 
  
  Explanation :
    1 2 3 4 5
    3 5 7 9
    8 12 16
    20 28
    48
    1+2=3, 2+3=5, 3+4=7, 4+5=9.
    Then 3+5=8, 5+7=12, 7+9=16.
    Then 8+12=20,12+16=28 then 20+28=48.
    4+8=12 then 1+2=3.
    
    Example Input/Output 2:
        Input: 4 1 6 2 9 Output: 7
            
        Explanation: 1 6 2 9 7 8 11 15 19 34
        1+6=7, 6+2=8, 2+9=11 then 7+8=15, 8+11=19 then 15+19=34.
Then 3+4=7.






# https://ide.geeksforgeeks.org/trVLGnoFks
