https://ide.geeksforgeeks.org/sGkEbQrHda


# An element is leader if it is greater than all the elements to 
# its right side. And the rightmost element is always a leader.
# For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2. 
a=list(map(int,input().split()))
max=a[-1]
print(max,end=" ")
# traverse in reverse order

for i in range(len(a)-2,0,-1):
    # max =2 //print
    # 5>2 //print
    # max=5 
    # 3 !>5 
    # max=5 
    # 4 > 5 no 
    # 17> 5 yes max =17 //print
    # 16>17 no 
    if(a[i]>max):
        print(a[i],end=" ")
        max=a[i]
            

          
