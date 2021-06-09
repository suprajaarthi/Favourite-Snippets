# Given two stings ransomNote and magazine, 
# return true if ransomNote can be constructed from magazine 
# and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

https://leetcode.com/problems/ransom-note/
 

ransomNote = "a";magazine = "b"
for x in ransomNote:
    if x not in magazine:
        print("False")
        quit()
    else:
        magazine=magazine.replace(x, '1', 1)
        
print("True")



  
https://ide.geeksforgeeks.org/p7vUMPmRcb
