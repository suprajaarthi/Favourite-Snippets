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

'amma'
a=[];   i='a'
a=[a];  i='m'
a=[a,m];i='m'
Here i=a[-1] => a.pop() a=[a]
a=['a'], i ='a'
a.pop()
Returns empty string 

# IP : ammar
#     After removing mm as the adjacent characters are same
#     ammar => aar
#     aar => r
# OP :   r
