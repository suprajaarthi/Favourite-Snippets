https://ide.geeksforgeeks.org/DBOI5KKryH

# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.


nums=list(map(int,input().split()))
sumVal = ret = 0
for i in nums: 
    sumVal = max(0, sumVal) + i 
    # print(sumVal)
    ret = max(ret, sumVal) 
    # print(ret)
print(max(nums) if ret == 0 else ret)


# Input: [-2,1,-3,4,-1,2,1,-5,4],
