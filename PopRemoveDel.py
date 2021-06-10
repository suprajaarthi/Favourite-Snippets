# https://ide.geeksforgeeks.org/ztRzUzVXAU 
  
  
#  remove() removes the first matching value/object.
#  It does not do anything with the indexing.

myList = [1, 2, 3, 2] 
myList.remove(2) 
print(myList) #[1, 3, 2]


# del removes the item at a specific index.

myList1 = [3, 2, 4, 1] 
del myList1[1] 
print(myList1) #[3, 2, 1]

# And pop removes the item at a specific index and returns it.

myList2 = [4, 3, 5] 
popped_val=myList2.pop(1) 
print(myList2) #[4, 5]
print(popped_val)


https://www.csestack.org/difference-between-remove-del-pop-python-list/
