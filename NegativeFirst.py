# https://ide.geeksforgeeks.org/RHjs4xWlWQ

def rearrange(arr, n ) :
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            # initially j is 0 and assign negative nos to the 1st index and 
            # then increment j 
            arr[j]= temp
            j = j + 1
    print(arr)
 
# Driver code
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)

# op : [-1, -3, -7, 4, 5, 6, 2, 8, 9]
