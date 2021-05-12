nums=list(map(int,input().split()))
nums.sort()
print(nums)
length = len(nums)
result = set()
for i in range(length-2):
    left = i+1
    right = length-1
    while left < right:
        sum_value = nums[i]+nums[left]+nums[right]
        # print(i,left,right,end=" ")
        # print(nums[i],nums[left],nums[right],end=" ")
        # print("")
        if sum_value == 0:
            result.add((nums[i],nums[left],nums[right]))
            left += 1
            right -= 1
        elif sum_value < 0:
            left +=1
        else:
            right -= 1
        # print(sum_value)
print(result)

# iven array nums = [-1, 0, 1, 2, -1, -4],
# https://ide.geeksforgeeks.org/HxyFjY6Ktr
