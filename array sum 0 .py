def printAllSublists(A):
 
    # consider all sublists starting from `i`
    for i in range(len(A)):
        sum = 0
        # consider all sublists ending at `j`
        for j in range(i, len(A)):
            # sum of elements so far
            sum += A[j]
            # if the sum is seen before, we have found a sublist with zero-sum
            if sum == 0:
                print("Sublist", (i, j))
 
 
if __name__ == '__main__':
 
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSublists(A)
# https://www.techiedelight.com/find-sub-array-with-0-sum/
