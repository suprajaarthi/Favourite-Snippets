# https://ide.geeksforgeeks.org/den11MEtBk
s=input().strip()
if s in s[1:]+s[:-1]:
    print("True")
else:
    print("False")
Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
