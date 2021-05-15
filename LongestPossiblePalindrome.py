# https://ide.geeksforgeeks.org/0fRQnt3ZtO
s='ttissaepeassitt'
palin_counter = 0
char_dict = {}
        
for char in s:
    char_dict[char] = char_dict.get(char, 0) + 1

for char_count in char_dict.values():
    palin_counter += (char_count // 2) * 2
        
if palin_counter < len(s): # must have had >0 odd counts
    palin_counter += 1
        
print(palin_counter)

# ip : ttissaepeassitt 
# op : 15 ( whole str is palindrome )
