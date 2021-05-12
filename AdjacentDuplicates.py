S=input().strip()
a=['']
for i in (S):
    if i!=a[-1]:
        a.append(i)
    else:
        a.pop()
        

# print(a)
print(''.join(a))
