https://ide.geeksforgeeks.org/cBrl72r7IP

# nums=list(map(int,input().split()))
nums=[1,5,1,2,3,5,3,4,6,4]
nums=sorted(nums)
i=0
while i<len(nums)-1 :
    if nums[i]==nums[i+1] :
        nums.pop(i)
    else :
        i+=1

print(len(nums))
print(nums)


# op : [1, 2, 3, 4, 5, 6]

 
