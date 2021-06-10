https://ide.geeksforgeeks.org/MHcICyNWb1

target=list(map(int,input().split()))
n=int(input())
res, pointer = [], 0
        
for val in range(1, n+1):
    if pointer == len(target):
        break
    elif val == target[pointer]:
        res += ['Push']
        pointer += 1
    else:
        res += ["Push", "Pop"]
print(res)


# 1 3 
# push 1 
# push 2 pop 2 
# push 3 
# => [ push, push , pop, push]


  
  
  
  
  
