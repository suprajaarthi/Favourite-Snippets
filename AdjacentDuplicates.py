https://ide.geeksforgeeks.org/TF50SQdfHL 
    
    
S=input().strip()
a=['']
for i in (S):
    if i!=a[-1]:
        a.append(i)
    else:
        a.pop()
        

# print(a)
print(''.join(a))


# IP : ammar
#     After removing mm as the adjacent characters are same
#     ammar => aar
#     aar => r
# OP :   r
