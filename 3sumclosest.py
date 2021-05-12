nums=list(map(int,input().split()))
target=int(input())
nums.sort()
ans = sum(nums[:3])
print(nums)
print(ans)
for i in range(len(nums)-2):
    k = len(nums)-1 
    j = i + 1 
    while j < k:
        close_sum = nums[i] + nums[j] + nums[k]
                
        if close_sum == target:
           print(close_sum)
                
        if abs(close_sum - target) < abs(ans - target):
            ans = close_sum
                
        if close_sum < target:
            j += 1
            
        elif close_sum > target: 
            k -= 1
        else: 
            break

print(ans)

# https://ide.geeksforgeeks.org/mLHid7ig3o
# https://leetcode.com/problems/3sum-closest/
