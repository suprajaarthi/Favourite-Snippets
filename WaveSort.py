https://ide.geeksforgeeks.org/cvKMnmwgBT
 

arr = [10, 90, 49, 2, 1, 5, 23]
n=len(arr)
arr.sort()
# sorted [1,2,5,10,23,49,90]
# sort an array in wave form
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
for i in range(0,n-1,2):
        
    arr[i], arr[i+1] = arr[i+1], arr[i]
 
print(arr)

# op : [2, 1, 10, 5, 49, 23, 90]
